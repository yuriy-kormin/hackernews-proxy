from urllib.parse import urljoin
import httpx
from bs4 import BeautifulSoup
from quart import Response
from app.config import ORIGIN_URL


async def get_soup_or_response(url_path):
    async with httpx.AsyncClient() as client:
        response = await client.get(urljoin(ORIGIN_URL, url_path))
        content_type = get_content_type(response)
        if 'text/' in content_type:
            return BeautifulSoup(response.text, 'lxml')
    return Response(response.content, content_type=content_type)


def get_content_type(response):
    return response.headers.get('Content-Type', '').lower()


async def fetch_headers(url):
    async with httpx.AsyncClient() as client:
        response = await client.head(url)
        content_type = response.headers.get('Content-Type')

    return content_type