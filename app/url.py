import logging
from urllib.parse import urljoin
import httpx
from bs4 import BeautifulSoup
from quart import Response
from app.config import ORIGIN_URL
from aiologger import Logger

logger = Logger.with_default_handlers()


async def get_soup_or_response(url_path):
    full_url = urljoin(ORIGIN_URL, url_path)
    content_type = await get_content(full_url, type='header')
    content = await get_content(full_url, type='page')
    print(f'{content_type=}')
    if 'text/html' in content_type:
        return BeautifulSoup(content.text, 'lxml')
    return Response(content.content, content_type=content_type)


async def get_content(url, type):
    async with httpx.AsyncClient() as client:
        if type == 'header':
            response = await client.head(url)

            print(f"{response.headers=}")
            return response.headers.get('Content-Type', '').lower()
        return await client.get(url)
