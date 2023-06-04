from flask import Flask, request
from bs4 import BeautifulSoup
from parser import process_tags, update_symlinks
from url import get_soup_or_response

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    soup = get_soup_or_response(request.full_path)
    if isinstance(soup, BeautifulSoup):
        process_tags(soup)
        update_symlinks(soup)
        return str(soup)
    return soup


if __name__ == '__main__':
    app.run()
