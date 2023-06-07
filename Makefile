install:
	poetry install --no-dev
install-dev:
	poetry install
test:
	poetry run pytest
lint:
	poetry run flake8 app
start:
	poetry run quart --app app.app run
