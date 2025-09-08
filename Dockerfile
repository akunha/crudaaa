# Usa una imagen oficial de Python como base
FROM python:3.9-slim

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
