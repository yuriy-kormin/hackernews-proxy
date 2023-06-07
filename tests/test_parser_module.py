from app.parser import process_tags, update_symlinks
from bs4 import BeautifulSoup
from app.config import ORIGIN_URL, PROXY_URL
from urllib.parse import urljoin
import pytest

@pytest.mark.asyncio
async def test_tags_change(get_qa_root_html):
    orig_html, result = get_qa_root_html
    soup = BeautifulSoup(orig_html, 'lxml')
    await process_tags(soup)
    assert str(soup) == result

@pytest.mark.asyncio
async def test_symlink_change(get_qa_root_html):
    pass