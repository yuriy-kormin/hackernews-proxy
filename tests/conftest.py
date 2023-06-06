import pytest
from app.app import app

FAKE_HTML = (
    'tests/fixtures/root_page.html',
    'tests/fixtures/root_page_correct_result.html'
)

FAKE_HTML_HREF = (
    'tests/fixtures/root_page_with_symlinks.html',
    'tests/fixtures/root_page_with_symlinks_result.html'
)


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def get_qa_root_html():
    return tuple(get_fixture_content(path) for path in FAKE_HTML)


@pytest.fixture
def get_qa_href_html():
    return tuple(get_fixture_content(path) for path in FAKE_HTML_HREF)


def get_fixture_content(path):
    with open(path, 'r') as file:
        return file.read()
