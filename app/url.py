from urllib.parse import urljoin
import httpx
from bs4 import BeautifulSoup
from quart import Response
from app.config import ORIGIN_URL
from app.logger import logger


async def get_soup_or_response(url_path):
    full_url = urljoin(ORIGIN_URL, url_path)
    response = await get_content(full_url)
    if content_type := await is_not_html(response):
        logger.debug(f'{full_url} is not a html. skip parsing')
        return Response(response.content, content_type=content_type)
    logger.debug(f'{full_url} is  html. Process parsing')
    return BeautifulSoup(response.text, 'lxml')


async def is_not_html(response):
    content_type = response.headers.get('Content-Type', '').lower()
    if 'text/html' not in content_type:
        return content_type


async def get_content(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)
