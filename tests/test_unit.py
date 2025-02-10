# tests/test_unit.py
import pytest
from app.app import app
from classifier.number_classifier import classify_number, is_armstrong, is_prime

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    with TestClient(app) as client:
        yield client

def test_classify_number():
    result = classify_number(371)
    assert result["number"] == 371
    assert "armstrong" in result["properties"]

def test_is_armstrong():
    assert is_armstrong(371) == True
    assert is_armstrong(123) == False

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(10) == False