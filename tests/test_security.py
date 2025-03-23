# tests/test_security.py
import pytest
import requests

def test_sql_injection():
    # Simula un intento de inyección SQL
    response = requests.get("http://localhost:5000/user?id=1' OR '1'='1")
    assert "error" in response.json(), "Endpoint vulnerable to SQL injection"