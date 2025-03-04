# Simple Flask App with Security Focus

## Description
This is a simple Flask application that demonstrates basic functionality while emphasizing security best practices. The app includes:
- A root route (`/`) that returns "Hello, world!".
- A dynamic route (`/hello/<name>`) that greets the user by name, with input validation to ensure the name contains only letters.

The project is built with a CI/CD pipeline that integrates security tools like Bandit, Safety, Gitleaks, and Trivy, as well as unit testing with Pytest and Codecov.

## Features
- **Input Validation**: The `/hello/<name>` route ensures that the name contains only alphabetic characters.
- **Security Scanning**: The CI/CD pipeline includes security checks for code vulnerabilities, dependency issues, and exposed secrets.
- **Unit Testing**: Comprehensive tests ensure the application behaves as expected.
- **Docker Integration**: The app is containerized and scanned for vulnerabilities before being pushed to Docker Hub.

## Prerequisites
- Python 3.9
- Docker
- Accounts and tokens for:
  - Docker Hub
  - Codecov
  - Gitleaks (if needed)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/app.git
cd app
```
### 2. Install Dependencies

```bash
Copy
python -m pip install --upgrade pip
pip install -r requirements.txt

```
### 3. Configure Environment Variables
Create a .env file if needed for any environment-specific configurations.

### 4. Run the Application Locally

```bash

python app.py
The app will be available at http://localhost:5000

```

#### 5. Run Tests

```bash

pytest tests/

```
### 6. Build and Run with Docker

```bash

docker build -t app-image:latest -f Dockerfile.app .
docker run -p 5000:5000 app-image:latest
```

CI/CD Pipeline
The pipeline is defined in .github/workflows/ci-cd.yml and includes the following steps:

1. Security Checks
Bandit: Scans the code for common security issues.

Safety: Checks dependencies for known vulnerabilities.

Gitleaks: Detects secrets or credentials exposed in the code.

2. Unit Testing
Pytest: Runs unit tests and generates a coverage report.

Codecov: Uploads the coverage report to Codecov for analysis.

3. Build and Push
Docker Build: Builds the Docker image.

Trivy: Scans the Docker image for vulnerabilities.

Docker Push: Pushes the image to Docker Hub.

Project Structure
```bash
app/
  __init__.py
  app.py
tests/
  test_app.py
Dockerfile.app
requirements.txt
.github/workflows/ci-cd.yml
.gitleaks.toml
```

Code Overview
app.py

```bash
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, mundo!"

@app.route('/hello/<name>')
def hello_name(name):
    if not name.isalpha():
        abort(400, description="El nombre solo puede contener letras.")
    return f"¡Hola, {name}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
test_app.py

```bash
import sys
import os

# Add the project path to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask app
from app import app

# Test for the root route
def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola, mundo!" in response.data

# Test for the /hello/<name> route
def test_hello_name():
    client = app.test_client()
    response = client.get('/hello/Fer')
    assert response.status_code == 200
    assert b"Hola, Fer!" in response.data

# Test for the /hello/<name> route with an invalid name
def test_hello_name_invalid():
    client = app.test_client()
    response = client.get('/hello/Fer123')
    assert response.status_code == 400
    assert b"El nombre solo puede contener letras." in response.data

```

Secrets and Tokens
Secrets are managed using GitHub Secrets. Ensure the following secrets are configured in your repository:

DOCKER_HUB_USERNAME

DOCKER_HUB_TOKEN

CODECOV_TOKEN

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.



