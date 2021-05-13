FROM python:3

WORKDIR /app

RUN pip install flask pyyaml
COPY ./app.py app.py

CMD ["python", "app.py"]