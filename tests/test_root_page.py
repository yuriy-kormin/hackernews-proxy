import httpretty
from app.config import ORIGIN_URL


@httpretty.activate(verbose=True)
def test_root_page(get_qa_root_html, client):
    origin_page, result_page = get_qa_root_html
    httpretty.register_uri(
        httpretty.GET, ORIGIN_URL,
        body=origin_page,
    )
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.text == result_page
