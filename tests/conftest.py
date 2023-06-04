import pytest

from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def get_qa_root_html():
    return tuple(
        get_fixture_content(path) for path in
        (FAKE_HTML, FAKE_HTML_RESULT)
    )


def get_fixture_content(path):
    with open(path, 'r') as file:
        return file.read()


FAKE_HTML = 'tests/fixtures/root_page.html'
FAKE_HTML_RESULT = 'tests/fixtures/root_page_correct_result.html'
