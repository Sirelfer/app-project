# Simple Flask App with Security Focus

![Badge](https://img.shields.io/badge/DevSecOps-Active-brightgreen)
![Badge](https://img.shields.io/badge/Python-3.9-blue)
![Badge](https://img.shields.io/badge/Docker-Supported-blue)
![Badge](https://img.shields.io/badge/Secure-With%20Trivy%20&%20Bandit-brightgreen)

This project is a **Python application** that uses the secure base Docker image provided by the [base project](https://github.com/yourusername/base-project). It is designed with a focus on **security**, **efficiency**, and **DevSecOps best practices**

This application demonstrates basic functionality while emphasizing **security best practices**. The app includes:
- A root route (`/`) that returns a customizable greeting using a template.
- A dynamic route (`/hello/<name>`) that greets the user by name, with input validation to ensure the name contains only letters.
- A CI/CD pipeline that integrates security tools like Bandit, Safety, Gitleaks, Trivy, Semgrep, and OWASP ZAP, as well as unit testing with Pytest and Codecov.

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
- [Security Enhancements](#security-enhancements)
- [Changelog](#changelog)
- [License](#license)

---

## Description

This is a **simple Flask application** designed to demonstrate **security best practices** in a Python web application. The app includes:


This is a simple Flask application designed to demonstrate security best practices in a Python web application. The app includes:

- **Input Validation**: Ensures that user input is safe and meets expected criteria.
- **Security Scanning**: Integrates multiple security tools to detect vulnerabilities in code, dependencies, and secrets.
- **Unit Testing**: Comprehensive tests to ensure the application behaves as expected.
- **Docker Integration**: The app is containerized and scanned for vulnerabilities before being pushed to Docker Hub.
- **DevSecOps Practices**: Implements a CI/CD pipeline with security scans, automated testing, and continuous monitoring.

## Features

- **Input Validation**: The `/hello/<name>` route ensures that the name contains only alphabetic characters, rejecting invalid input with a `400` response.
- **Security Headers**: Implements HTTP security headers (e.g., CSP, X-Frame-Options) to mitigate common web vulnerabilities.
- **Security Scanning**:
  - **Bandit**: Static code analysis for Python.
  - **Safety**: Dependency vulnerability scanning.
  - **Gitleaks**: Detects secrets in the code.
  - **Trivy**: Scans Docker images for vulnerabilities.
  - **Semgrep**: Advanced static analysis for code security.
  - **OWASP ZAP**: Dynamic application security testing (DAST) for web vulnerabilities.
- **Unit Testing**: Uses Pytest for unit tests and Codecov for coverage reporting.
- **Docker Integration**: The app is containerized and optimized for secure deployment.
- **CI/CD Pipeline**: Automates testing, security scans, and deployment using GitHub Actions.

## Prerequisites

- **Python 3.9**
- **Docker**
- **Accounts and Tokens**:
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

    *  Bandit: Scans the code for common security issues.
    *  Safety: Checks dependencies for known vulnerabilities.
    *  Gitleaks: Detects secrets or credentials exposed in the code.
    *  Semgrep: Performs advanced static analysis to detect code vulnerabilities (e.g., insecure Flask configurations).
    *  OWASP ZAP: Runs dynamic security scans to identify web vulnerabilities (e.g., XSS, clickjacking).
    *  Trivy: Scans Docker images for vulnerabilities.

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

* Semgrep: Reports code-level vulnerabilities (e.g., insecure Flask app.run configurations) in semgrep-results.sarif.

* OWASP ZAP: Generates a report (zap-report.html) with web vulnerabilities (e.g., missing CSP headers).
 
* Pytest/Codecov: Test failures will fail the pipeline, and coverage reports are uploaded to Codecov.

## Project Structure

```bash
app/
  __init__.py
  app.py
tests/
  test_app.py
templates/
  index.html
Dockerfile.app
requirements.txt
.github/workflows/ci-cd.yml
.gitleaks.toml
```

## Code Overview

app.py

```bash
import re
from flask import Flask, request, render_template

app = Flask(__name__)

# Middleware para agregar encabezados de seguridad
@app.after_request
def apply_security_headers(response):
    """Agrega encabezados de seguridad a todas las respuestas."""
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'none'; form-action 'self'"
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, private'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Server'] = 'WebServer'
    return response

@app.route('/')
def hello():
    """Ruta principal que renderiza una plantilla con un nombre de usuario desde query params."""
    nombre = request.args.get('nombre', 'Usuario')
    return render_template('index.html', nombre=nombre)

@app.route('/hello/<name>')
def hello_name(name):
    """Ruta que renderiza un saludo personalizado para un nombre dado en la URL."""
    if not re.match("^[a-zA-Z]+$", name):
        return "El nombre solo puede contener letras.", 400
    return render_template('index.html', nombre=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
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
    assert b"<h1>Bienvenido, Usuario</h1>" in response.data

# Test for the /hello/<name> route
def test_hello_name():
    client = app.test_client()
    response = client.get('/hello/Fer')
    assert response.status_code == 200
    assert b"<h1>Bienvenido, Fer</h1>" in response.data

# Test for the /hello/<name> route with an invalid name
def test_hello_name_invalid():
    client = app.test_client()
    response = client.get('/hello/Fer123')
    assert response.status_code == 400
    assert b"El nombre solo puede contener letras." in response.data
```
templates/index.html

```bash
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Bienvenida</title>
</head>
<body>
    <h1>Bienvenido, {{ nombre }}</h1>
</body>
</html>
```

## Secrets and Tokens
Secrets are managed using GitHub Secrets. Ensure the following secrets are configured in your repository:

* DOCKER_HUB_USERNAME

* DOCKER_HUB_TOKEN

* CODECOV_TOKEN

## Security Enhancements

This project incorporates several security improvements, following DevSecOps best practices:

* Semgrep Fixes:
    * Restricted Flask app.run to host='127.0.0.1' to prevent exposure to external networks (Rule: python.flask.security.audit.app-run-param-config, OWASP A01:2021 - Broken Access Control).
    * Replaced direct string formatting with render_template to prevent XSS vulnerabilities (Rule: python.flask.security.audit.directly-returned-format-string, OWASP A03:2021 - Injection).

* OWASP ZAP Fixes:
    * Added Content-Security-Policy header with default-src 'self'; frame-ancestors 'none'; form-action 'self' to mitigate XSS and clickjacking (Alert #10038, Medium).
    * Added X-Frame-Options: DENY to prevent clickjacking (Alert #10020, Medium).
    * Added X-Content-Type-Options: nosniff to prevent MIME-sniffing (Alert #10021, Low).
    * Added Cross-Origin-Resource-Policy: same-origin to mitigate Spectre vulnerabilities (Alert #90004, Low).
    * Added Permissions-Policy to restrict browser features (Alert #10063, Low).
    * Overwrote Server header to hide version info (Alert #10036, Low).
    * Added Cache-Control, Pragma, and Expires to prevent caching of sensitive content (Alert #10049, Informational).

* Pipeline Improvements:
    * Configured ZAP to run in a Docker network with the app container, resolving connectivity issues (ZAP failed to access: http://localhost:8080).
    * Optimized pipeline to reduce duplicate executions by limiting triggers to pull_request events.

## Changelog
[1.1.0] - 2025-03-13
Added
* Security headers middleware in app.py to mitigate common web vulnerabilities.
* /hello/<name> route with name validation using regex.
* templates/index.html for rendering dynamic greetings. 
* Semgrep and OWASP ZAP scans in the CI/CD pipeline.
* Unit tests for root and dynamic routes with input validation.

Fixed
* Resolved Semgrep vulnerabilities:
    * Restricted Flask app.run to host='127.0.0.1' (OWASP A01:2021).
    * Used render_template to prevent XSS (OWASP A03:2021).
* Resolved OWASP ZAP vulnerabilities:
    * Added CSP with frame-ancestors and form-action directives.
    * Added anti-clickjacking, MIME-sniffing, and Spectre mitigations.
* Fixed test failures in test_app.py by aligning routes and assertions.
* Resolved ZAP connectivity issues in the pipeline.

License
This project is licensed under the MIT License. See the LICENSE file for details. 



