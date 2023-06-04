import re
from urllib.parse import urlparse, urlunparse
from app.config import WORD_LENGTH, ORIGIN_URL, PROXY_URL
ORIGIN_NETLOC = urlparse(ORIGIN_URL).netloc


def process_tags(soup):
    for tag in soup.find_all(
            string=lambda element: len(element) >= WORD_LENGTH):
        parse_tag(tag)


def parse_tag(tag):
    tag.replace_with(
        re.sub(r'((?:^|\s)\w{6})(?=(\s|$))', r'\1' + '™', tag)
    )


def update_symlinks(soup):
    for symlink in soup.find_all('a', href=True):
        modify_symlink(symlink)


def modify_symlink(symlink):
    parsed_url = urlparse(symlink['href'])
    if parsed_url.netloc == ORIGIN_NETLOC:
        parsed_url._replace(netloc=PROXY_URL)
        symlink['href'] = urlunparse(parsed_url)
