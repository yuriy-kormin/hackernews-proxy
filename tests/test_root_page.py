from pytest_httpx import HTTPXMock
from app.config import ORIGIN_URL
import pytest


@pytest.mark.asyncio
async def test_open_root_page(
        client,
        get_qa_root_html,
        httpx_mock: HTTPXMock
):
    origin_page, result_page = get_qa_root_html

    httpx_mock.add_response(
        url=ORIGIN_URL,
        html=origin_page,
        status_code=200,
    )
    resp = await client.get('/')
    assert resp.status_code == 200
    resp_data = await resp.get_data(as_text=True)
    assert resp_data == result_page

@pytest.mark.asyncio
async def test_symlink_modificataion(
        client,
        get_qa_root_html,
        httpx_mock: HTTPXMock
):
    origin_page, result_page = get_qa_root_html

    httpx_mock.add_response(
        url=ORIGIN_URL,
        html=origin_page,
        status_code=200,
    )
    resp = await client.get('/')
    assert resp.status_code == 200
    resp_data = await resp.get_data(as_text=True)
    assert resp_data == result_page
