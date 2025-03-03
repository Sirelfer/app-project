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
    app.run(host='127.0.0.1', port=5000)