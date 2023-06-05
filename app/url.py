from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from flask import Response
from app.config import ORIGIN_URL


def get_soup_or_response(url_path):
    response = requests.get(
        urljoin(ORIGIN_URL, url_path)
    )
    content_type = get_content_type(response)
    if 'text/' in content_type:
        return BeautifulSoup(response.text, 'lxml')
    return Response(response.content, content_type=content_type)


def get_content_type(response):
    return response.headers.get('Content-Type', '').lower()
