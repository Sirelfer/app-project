# Simple Flask App with Security Focus

![Badge](https://img.shields.io/badge/DevSecOps-Active-brightgreen)
![Badge](https://img.shields.io/badge/Python-3.9-blue)
![Badge](https://img.shields.io/badge/Docker-Supported-blue)
![Badge](https://img.shields.io/badge/Secure-With%20Trivy%20&%20Bandit-brightgreen)

This project is a **Python application** that uses the secure base Docker image provided by the [base project](https://github.com/yourusername/base-project). It is designed with a focus on **security**, **efficiency**, and **DevSecOps best practices**

This application demonstrates basic functionality while emphasizing **security best practices**. The app includes:
- A root route (`/`) that returns "Hello, world!".
- A dynamic route (`/hello/<name>`) that greets the user by name, with input validation to ensure the name contains only letters.

The project is built with a **CI/CD pipeline** that integrates security tools like **Bandit**, **Safety**, **Gitleaks**, and **Trivy**, as well as unit testing with **Pytest** and **Codecov**.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [CI/CD Pipeline](#cicd-pipeline)
- [Project Structure](#project-structure)
- [Code Overview](#code-overview)
- [Secrets and Tokens](#secrets-and-tokens)
- [License](#license)

---

## Description

This is a **simple Flask application** designed to demonstrate **security best practices** in a Python web application. The app includes:


- **Input Validation**: Ensures that user input is safe and meets expected criteria.
- **Security Scanning**: Integrates multiple security tools to detect vulnerabilities in code, dependencies, and secrets.
- **Unit Testing**: Comprehensive tests to ensure the application behaves as expected.
- **Docker Integration**: The app is containerized and scanned for vulnerabilities before being pushed to Docker Hub.

---

## Features

- **Input Validation**: The `/hello/<name>` route ensures that the name contains only alphabetic characters.
- **Security Scanning**:
  - **Bandit**: Static code analysis for Python.
  - **Safety**: Dependency vulnerability scanning.
  - **Gitleaks**: Detects secrets in the code.
  - **Trivy**: Scans Docker images for vulnerabilities.
- **Unit Testing**: Uses **Pytest** for unit tests and **Codecov** for coverage reporting.
- **Docker Integration**: The app is containerized and optimized for secure deployment.

---

## Prerequisites

- **Python 3.9**
- **Docker**
- **Accounts and Tokens**:
  - Docker Hub
  - Codecov
  - Gitleaks (if needed)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/app.git
cd app
```
### 2. Install Dependencies

```bash

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

## CI/CD Pipeline

The pipeline is defined in .github/workflows/ci-cd.yml and includes the following steps:

### Pipeline Stages

1. Security Checks:

    * Bandit: Scans the code for common security issues.

    * Safety: Checks dependencies for known vulnerabilities.

    * Gitleaks: Detects secrets or credentials exposed in the code.

2. Unit Testing:

    * Pytest: Runs unit tests and generates a coverage report.

    * Codecov: Uploads the coverage report to Codecov for analysis.

3. Build and Push:

    * Docker Build: Builds the Docker image.

    * Trivy: Scans the Docker image for vulnerabilities.

    * Docker Push: Pushes the image to Docker Hub.

## How to Interpret Results

* Bandit: If issues are found, the pipeline will fail, and a detailed report will be available in the logs.

* Safety: If insecure dependencies are detected, the pipeline will fail, and a report will be generated.

* Gitleaks: If secrets are detected, the pipeline will fail, and a report will be generated.

* Trivy: If vulnerabilities are found, the pipeline will fail, and a detailed report will be available.

## Project Structure

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

## Code Overview

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

## Secrets and Tokens
Secrets are managed using GitHub Secrets. Ensure the following secrets are configured in your repository:

* DOCKER_HUB_USERNAME

* DOCKER_HUB_TOKEN

* CODECOV_TOKEN

License
This project is licensed under the MIT License. See the LICENSE file for details.



