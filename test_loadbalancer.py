import pytest
from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_mango(client):
    result = client.get("/", headers={'Host': 'www.mango.com'})
    assert b'this is mango application' in result.data


def test_host_routing_apple(client):
    result = client.get("/", headers={'Host': 'www.apple.com'})
    assert b'this is apple application' in result.data


def test_host_routing_not_found(client):
    result = client.get('/', headers={'Host': 'www.notmango.com'})
    assert b'Not Found' in result.data
    assert 404 == result.status_code

# path based routing tests


def test_path_routing_mango(client):
    result = client.get("/mango")
    assert b'this is mango application' in result.data


def test_path_routing_apple(client):
    result = client.get("/apple")
    assert b'this is apple application' in result.data


def test_path_not_found(client):
    result = client.get("/notmango")
    assert b'Not Found' in result.data
    assert 404 == result.status_code

