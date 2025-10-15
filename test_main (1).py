import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={"username": "admin", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_enqueue_task():
    login_response = client.post("/login", json={"username": "admin", "password": "password"})
    token = login_response.json()["access_token"]
    response = client.post("/tasks", json={"task": "scan data"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["status"] == "queued"