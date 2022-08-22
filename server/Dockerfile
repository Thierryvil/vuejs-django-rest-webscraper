FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080