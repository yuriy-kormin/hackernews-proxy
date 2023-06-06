import httpretty
from app.config import ORIGIN_URL
import pytest
from app.app import app
from quart.testing import QuartClient

# @httpretty.activate(verbose=True)
@pytest.mark.asyncio
async def test_root_page(client, get_qa_root_html):
    origin_page, result_page = get_qa_root_html
    httpretty.enable()
    httpretty.register_uri(
        httpretty.GET, ORIGIN_URL,
        body=origin_page,
    )
    # async with app.test_client() as client:
    resp = await client.get('/')
    assert resp.status_code == 200
    assert resp.text == result_page




