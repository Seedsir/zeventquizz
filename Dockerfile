FROM python:3.12-bookworm

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000
CMD gunicorn --config gunicorn.conf.py