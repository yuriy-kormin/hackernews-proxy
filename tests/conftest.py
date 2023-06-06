import pytest
from app.app import app

FAKE_HTML = (
    'tests/fixtures/root_page.html',
    'tests/fixtures/root_page_correct_result.html'
)

@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def get_qa_root_html():
    return tuple(get_fixture_content(path) for path in FAKE_HTML)


def get_fixture_content(path):
    with open(path, 'r') as file:
        return file.read()
