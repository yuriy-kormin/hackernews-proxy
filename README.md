[![Test](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/run_tests.yml/badge.svg)](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/run_tests.yml)
[![Coverage](https://github.com/yuriy-kormin/hackernews-proxy/blob/master/.cov/coverage.svg)](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/calculate_coverage.yml)
[![Linter](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/run_lint.yml/badge.svg)](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/run_lint.yml)
[![Docker Compose Build and Test](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/docker-build-test.yml/badge.svg)](https://github.com/yuriy-kormin/hackernews-proxy/actions/workflows/docker-build-test.yml)
# Hackernews Proxy

This repository contains my solution for the code challenge by Ivelum. The challenge description can be found [here](https://github.com/ivelum/job/blob/master/challenges/python.md).

The Hackernews Proxy is a web application that processes pages from the site [Hacker News](https://news.ycombinator.com/) and adds a ™ symbol after each word on the page whose length is equal to the configured value (6 by default). The proxy utilizes the [BeautifulSoup library](https://pypi.org/project/beautifulsoup4/) for parsing the web pages and Quart, an asynchronous version of Flask, for handling requests.

## Installation

To install and run the Hackernews Proxy, follow these steps:

```bash
git clone https://github.com/yuriy-kormin/hackernews-proxy.git
cd hackernews-proxy
docker-compose up --build
```

## USAGE

Once the Docker containers are up and running, you can access the Hackernews Proxy by opening a web browser and navigating to http://localhost.


## Additional Settings

The Hackernews Proxy provides some additional settings that you can customize:

- **NGINX_PORT** (default: 80): By default, the application responds on port 80. You can modify this setting by updating the `NGINX_PORT` variable in the `.env` file located in the root directory of the project. After making changes, the application will be accessible on a different address, such as `http://localhost:NGINX_PORT`.

- **WORD_LENGTH**: The `WORD_LENGTH` setting determines the length of the words to which the ™ symbol will be added. By default, this value is set to 6, as specified in the original task. However, you can modify it to any other desired value by updating the `WORD_LENGTH` variable in the `app/config.py` file.

Feel free to customize these settings according to your requirements.
