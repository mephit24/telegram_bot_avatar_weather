FROM python:3.10-slim-bullseye

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get -y install libcairo2-dev
RUN python -m pip install -r requirements.txt

CMD python app.py
