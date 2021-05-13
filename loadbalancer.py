import random
from flask import Flask, request
import requests


loadbalancer = Flask(__name__)

apple_backends = ["localhost:9081", "localhost:9082"]
mango_backends = ["localhost:8081", "localhost:8082"]


@loadbalancer.route("/")
def router():
    host_header = request.headers["Host"]
    if host_header == "www.mango.com":
        response = requests.get(f"http://{random.choice(mango_backends)}")
        return response.content, response.status_code

    elif host_header == "www.apple.com":
        response = requests.get(f"http://{random.choice(apple_backends)}")
        return response.content, response.status_code
    else:
        return 'Not Found', 404
