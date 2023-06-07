from quart import Quart, request
from bs4 import BeautifulSoup
from app.parser import process_tags, update_symlinks
from app.url import get_soup_or_response

app = Quart(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
async def proxy(path):
    full_path = path + '?' + request.query_string.decode()
    soup = await get_soup_or_response(full_path)
    if isinstance(soup, BeautifulSoup):
        await process_tags(soup)
        await update_symlinks(soup)
        return str(soup)
    return soup


if __name__ == '__main__':
    app.run()
