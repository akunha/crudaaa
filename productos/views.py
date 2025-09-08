from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def home(request):
    return render(request, 'productos/home.html')  # Asegúrate de crear esta plantilla

# Vista para mostrar todos los productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar.html', {'productos': productos})

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/formulario.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})


def crear_producto_usuario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el producto
            return redirect('listar_productos')  # Redirigir a la lista de productos
    else:
        form = ProductoForm()  # Mostrar formulario vacío
    return render(request, 'productos/formulario_usuario.html', {'form': form})
