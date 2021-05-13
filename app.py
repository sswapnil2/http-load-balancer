from flask import Flask
import os

app = Flask(__name__)


@app.get("/")
def index():
    return f'this is {os.environ["APPLICATION"]} application'


if __name__ == '__main__':
    app.run("0.0.0.0")