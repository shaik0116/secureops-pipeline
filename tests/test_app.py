import pytest
from app.app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_healthy_status(client):
    data = response = client.get("/health").get_json()
    assert data["status"] == "healthy"


def test_get_user_returns_200(client):
    response = client.get("/api/user?username=testuser")
    assert response.status_code == 200


def test_ping_returns_200(client):
    response = client.post("/api/ping", json={"host": "127.0.0.1"})
    assert response.status_code == 200


def test_secret_endpoint_returns_200(client):
    response = client.get("/api/secret?name=test-secret")
    assert response.status_code == 200
