from app.parser import process_tags, update_symlinks
from bs4 import BeautifulSoup


def test_tags_change(get_qa_root_html):
    orig_html, result = get_qa_root_html
    soup = BeautifulSoup(orig_html, 'lxml')
    process_tags(soup)
    assert str(soup) == result
