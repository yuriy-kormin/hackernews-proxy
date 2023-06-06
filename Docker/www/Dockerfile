FROM python:slim-buster
WORKDIR /app
COPY ["pyproject.toml","README.md","poetry.lock","/poetry/"]
WORKDIR /poetry

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install hypercorn && \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

CMD ["hypercorn",  "app.app:app", "-w", "4", "--bind", "0.0.0.0:5000"]
