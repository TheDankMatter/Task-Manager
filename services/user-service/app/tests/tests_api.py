from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "id": 1,
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "is_active": True
    })
    assert response.status_code == 201
    assert response.json()["username"] == "johndoe"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "johndoe"

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"