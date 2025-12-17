import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_redirect():
    response = client.get("/")
    assert response.status_code in (200, 307, 308)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_register_and_unregister():
    # Register a participant
    activity_id = 1
    participant = {"name": "Test User"}
    reg_response = client.post(f"/activities/{activity_id}/register", json=participant)
    assert reg_response.status_code == 200
    # Unregister the participant
    unreg_response = client.post(f"/activities/{activity_id}/unregister", json=participant)
    assert unreg_response.status_code == 200
