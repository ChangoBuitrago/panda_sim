FROM python:3.7-slim

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv --three
RUN pipenv install
COPY . .
RUN python -m compileall .
RUN pipenv run ./manage.py makemigrations
RUN pipenv run ./manage.py migrate

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
CMD ["web"]
