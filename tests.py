import pytest
import requests

# CRUD
BASE_URL = "http://localhost:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Test Task",
        "description": "This is a test task"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])  # Store the created task ID for cleanup