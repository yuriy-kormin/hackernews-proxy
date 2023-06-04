from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from flask import Response
from app.config import ORIGIN_URL


def get_soup_or_response(url_path):
    response = download_data(
        urljoin(ORIGIN_URL, url_path)
    )
    content_type = determine_content_type(response)
    if 'text/' in content_type:
        return make_soup(response.text)
    return Response(response.content, content_type=content_type)


def download_data(url):
    return requests.get(url)


def determine_content_type(response):
    return response.headers.get('Content-Type', '').lower()


def make_soup(data):
    return BeautifulSoup(data, 'lxml')
