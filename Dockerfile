FROM python:3.6-alpine

WORKDIR /Back-end-Informatica

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP main.py

CMD ["python3","-m","flask","run","--host=0.0.0.0"]