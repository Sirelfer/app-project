from flask import Flask, request, render_template

app = Flask(__name__)

@app.after_request
def apply_security_headers(response):
    """Agrega encabezados de seguridad a todas las respuestas."""
    # CSP: Solo permite recursos del mismo origen
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    # Anti-clickjacking
    response.headers['X-Frame-Options'] = 'DENY'
    # Anti-MIME-sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Protección contra Spectre
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
    # Deshabilitar funciones del navegador no necesarias
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    # Evitar cacheo de respuestas sensibles
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, private'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    # Sobrescribir el encabezado Server para ocultar detalles
    response.headers['Server'] = 'WebServer'
    return response

@app.route('/')
def hello():
    nombre = request.args.get('nombre','Usuario')
    return render_template('index.html', nombre=nombre)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)