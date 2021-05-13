import random
from flask import Flask, request
import requests
import yaml


loadbalancer = Flask(__name__)


def load_configuration(file_path):

    with open(file_path) as config_file:
        _config = yaml.load(config_file, Loader=yaml.FullLoader)
    return _config


config = load_configuration("loadbalancer.yaml")


@loadbalancer.get("/")
def router():
    host_header = request.headers["Host"]
    for entry in config["hosts"]:
        if host_header == entry["host"]:
            response = requests.get(f"http://{random.choice(entry['servers'])}")
            return response.content, response.status_code

    return 'Not Found', 404


@loadbalancer.get("/<path>")
def path_router(path):

    for entry in config["paths"]:
        if ("/" + path) == entry["path"]:
            response = requests.get(f"http://{random.choice(entry['servers'])}")
            return response.content, response.status_code

    return 'Not Found', 404

