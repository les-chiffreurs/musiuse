FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install cron python3 python3-venv python3-pip tzdata

ENV TZ=Europe/Zurich
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN update-ca-certificates --fresh
ENV SSL_CERT_DIR /etc/ssl/certs

COPY python_scrapper /usr/local/python_scrapper
COPY requirements.txt /usr/local/requirements.txt

RUN python3 -m venv /usr/local/env
RUN . /usr/local/env/bin/activate
RUN pip install -r /usr/local/requirements.txt

COPY scrap-cron /etc/cron.d/scrap-cron

RUN chmod 0644 /etc/cron.d/scrap-cron

RUN crontab /etc/cron.d/scrap-cron

CMD ["cron", "-f"]
