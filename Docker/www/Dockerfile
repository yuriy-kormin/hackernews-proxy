FROM python:slim-buster

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install poetry && \
    poetry install --no-root

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]