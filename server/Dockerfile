FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]