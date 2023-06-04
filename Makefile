install:
	poetry install --no-dev
install-dev:
	poetry install
test:
	poetry run pytest -s
lint:
	poetry run flake8 app
start:
	poetry run flask --app app.app run
