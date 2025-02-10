import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app
#  pytests for the API

import pytest
from fastapi.testclient import TestClient


client = TestClient(app)

def test_classify_number():
    response = client.get("/api/classify-number/?number=371")
    assert response.status_code == 200
    assert response.json()["number"] == 371
    assert "armstrong" in response.json()["properties"]

def test_invalid_input():
    response = client.get("/api/classify-number/?number=abc")
    assert response.status_code == 400
    assert response.json()["detail"]["number"] == "alphabet"
    assert response.json()["detail"]["error"] == True