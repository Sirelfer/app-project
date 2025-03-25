# tests/test_security.py
import pytest
import requests

def test_sql_injection():
    # Simula un intento de inyección SQL
    response = requests.get("http://localhost:5000/?id=1' OR '1'='1")
    # Verifica que la respuesta sea la misma que para una solicitud normal
    normal_response = requests.get("http://localhost:5000/")
    assert response.status_code == 200, "Expected a 200 response"
    assert response.text == normal_response.text, "Response should not change with malicious input"
    assert "Hola Mundo" in response.text, "Expected 'Hola Mundo' in response"
