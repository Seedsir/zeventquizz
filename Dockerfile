FROM python:3.10-alpine
COPY . /app
WORKDIR /app
CMD pip install -r requirements.txt
ENTRYPOINT [ "python", "main2.py" ]