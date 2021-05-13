FROM python:3

WORKDIR /app

RUN pip install flask
COPY ./app.py app.py

CMD ["python", "app.py"]