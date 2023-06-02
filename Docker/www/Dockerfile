FROM python:slim-buster

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]