# tests/test_security.py
import pytest
import requests

def test_sql_injection():
    # Simula un intento de inyección SQL en un endpoint válido
    response = requests.get("http://localhost:5000/?id=1' OR '1'='1")
    # Verifica que la respuesta no sea un éxito (e.g., 200), lo que indicaría una posible vulnerabilidad
    assert response.status_code != 200, "Endpoint might be vulnerable to SQL injection"
    # Si esperas un mensaje de error específico, verifica el contenido del texto
    assert "error" in response.text.lower() or "invalid" in response.text.lower(), "Expected error message not found"