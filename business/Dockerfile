# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app

RUN apk update


RUN apk add libffi-dev jpeg-dev zlib-dev libffi gcc zlib-dev jpeg-dev gdal-dev musl-dev postgresql-dev
RUN apk add --no-cache geos gdal 

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 3000

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
