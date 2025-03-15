# Dockerfile.app
# Usar la imagen base personalizada
FROM elfer/base-image:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y la aplicación
COPY requirements.txt .
COPY . .

# Instalar dependencias, incluyendo Gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]