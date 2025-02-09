# docker build -t nibata/api:0.0.1 -f images/Dockerfile-FastAPI .
FROM python:3.12-slim
LABEL authors="nbacquet"

RUN rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin
RUN apt-get update

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD alembic upgrade head; uvicorn main:app --host 0.0.0.0 --port 80