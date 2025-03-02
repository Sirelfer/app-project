# Dockerfile.app
FROM elfer/base-image:latest

WORKDIR /app

# Copia el código de la aplicación
COPY . .

# Expone el puerto 5000 (por ejemplo, para Flask)
EXPOSE 5000

CMD ["python", "app.py"]