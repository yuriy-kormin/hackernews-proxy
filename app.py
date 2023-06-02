from flask import Flask, Response, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse, urljoin
import re

app = Flask(__name__)
proxy_url = 'http://localhost:5000'

WORD_LENGTH = 6


def process_tag(tag):
    tag.replace_with(
        re.sub(r'((?:^|\s)\w{6})(?=(\s|$))', r'\1' + '™', tag)
    )


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    path = request.full_path
    url = urljoin('https://news.ycombinator.com', path)
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', '').lower()
    if 'text/html' not in content_type:
        return Response(response.content, content_type=content_type)
    soup = BeautifulSoup(response.text, 'lxml')
    for tag in soup.find_all(
            string=lambda element: len(element) >= WORD_LENGTH):
        process_tag(tag)
    for tag in soup.find_all('a', href=True):
        parsed_url = urlparse(tag['href'])
        if parsed_url.netloc == 'news.ycombinator.com':
            parsed_url._replace(netloc=proxy_url)
            tag['href'] = urlunparse(parsed_url)
    return str(soup)


if __name__ == '__main__':
    app.run()
