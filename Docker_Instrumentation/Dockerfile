# This is the docker file for custom prometheis Docker application instrumentation
FROM tiangolo/uwsgi-nginx:python3.12

RUN pip install prometheus_client

ENV LISTEN_PORT=5001 

EXPOSE 5001

COPY ./app /app

WORKDIR /app
