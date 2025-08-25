FROM python:3.7-slim-buster

RUN apt-get update -y && apt-get install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
