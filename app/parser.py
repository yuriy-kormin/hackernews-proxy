import re
from urllib.parse import urlparse, urlunparse
from app.config import WORD_LENGTH, ORIGIN_URL, PROXY_URL
from app.url import logger

ORIGIN_NETLOC = urlparse(ORIGIN_URL).netloc
REPLACE_PATTERN = r'((?:^|\s)\w{6})(?=(\s|$))'


def process_tags(soup):
    logger.debug('processing page for add content')
    for tag in soup.find_all(
            string=lambda element: len(element) >= WORD_LENGTH):
        tag.replace_with(
            re.sub(REPLACE_PATTERN, r'\1' + '™', tag)
        )


def update_symlinks(soup):
    logger.debug('processing page for update symlinks')
    for symlink in soup.find_all('a', href=True):
        parsed_url = urlparse(symlink['href'])
        if parsed_url.netloc == ORIGIN_NETLOC:
            parsed_url._replace(netloc=PROXY_URL)
            symlink['href'] = urlunparse(parsed_url)
