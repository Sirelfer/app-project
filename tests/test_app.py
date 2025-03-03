import sys
import os

# Agrega la ruta del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa la aplicación Flask
from app import app

# Prueba para la ruta principal
def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola, mundo!" in response.data

# Prueba para la ruta /hello/<name>
def test_hello_name():
    client = app.test_client()
    response = client.get('/hello/Fer')
    assert response.status_code == 200
    assert b"Hola, Fer!" in response.data

# Prueba para la ruta /hello/<name> con un nombre inválido
def test_hello_name_invalid():
    client = app.test_client()
    response = client.get('/hello/Fer123')
    assert response.status_code == 400
    assert b"El nombre solo puede contener letras." in response.data



     