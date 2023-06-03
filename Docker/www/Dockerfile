FROM python:slim-buster

COPY ["pyproject.toml","README.md","poetry.lock","/poetry/"]
WORKDIR /poetry

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install gunicorn && \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]