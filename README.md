[![Run pytest](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/run_tests.yml/badge.svg)](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/run_tests.yml)
## Hackernews proxy

It's my solution for code challenge by Ivelum [https://github.com/ivelum/job/blob/master/challenges/python.md](https://github.com/ivelum/job/blob/master/challenges/python.md)

The proxy processes pages from the site  [Hacker News](https://news.ycombinator.com/) and uses the [BeautifulSoup library](https://pypi.org/project/beautifulsoup4/) to add a ™ sign after each word on the page, which length is equal to setted in configuration
(6 by default).

