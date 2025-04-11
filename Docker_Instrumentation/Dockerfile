FROM tiangolo/uwsgi-nginx:python3.12

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir flask prometheus_client

ENV LISTEN_PORT=5001
EXPOSE 5001
