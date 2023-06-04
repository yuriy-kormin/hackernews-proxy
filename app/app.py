from flask import Flask, Response, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse, urljoin
import re

from app.config import WORD_LENGTH, PROXY_URL, ORIGIN_URL

app = Flask(__name__)


def process_tags(soup):
    for tag in soup.find_all(
            string=lambda element: len(element) >= WORD_LENGTH):
        process_tag(tag)


def process_tag(tag):
    # print(f'{tag=}', file=sys.stderr)
    tag.replace_with(
        re.sub(r'((?:^|\s)\w{6})(?=(\s|$))', r'\1' + '™', tag)
    )


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    path = request.full_path
    url = urljoin(ORIGIN_URL, path)
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', '').lower()
    if 'text/' not in content_type:
        return Response(response.content, content_type=content_type)
    soup = BeautifulSoup(response.text, 'lxml')
    process_tags(soup)
    ORIGIN_NETLOC = urlparse(ORIGIN_URL).netloc
    for tag in soup.find_all('a', href=True):
        parsed_url = urlparse(tag['href'])
        if parsed_url.netloc == ORIGIN_NETLOC:
            parsed_url._replace(netloc=PROXY_URL)
            tag['href'] = urlunparse(parsed_url)
    return str(soup)


if __name__ == '__main__':
    app.run()
