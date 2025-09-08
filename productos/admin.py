# productos/admin.py
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)  # Registra el modelo Producto en el admin
