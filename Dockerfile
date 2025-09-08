# Usa una imagen oficial de Python 3.10 como base
FROM python:3.10-slim

# Instala las herramientas necesarias para psycopg2 (pg_config y dependencias)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt a la carpeta de trabajo
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto al contenedor
COPY . /app/

# Expone el puerto 5000 para que Railway pueda acceder a él
EXPOSE 5000

# Ejecuta el servidor Django con Gunicorn
CMD ["gunicorn", "crudAAA.wsgi:application", "--bind", "0.0.0.0:5000"]
