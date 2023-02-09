FROM python:3.8

RUN apt-get update \
  && apt-get install --no-install-recommends --assume-yes \
  gcc \
  libpq-dev \
  libffi-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]