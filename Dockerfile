FROM python:3.12.3

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc

# add app
COPY ../app/ .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/base.txt

CMD ./scripts/docker-entrypoint.sh
