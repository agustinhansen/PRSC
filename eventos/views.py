from django.shortcuts import render
from .models import Productos

# Una prueba

def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'eventos/productos.html', {'productos': productos})

def nuevo(request):
    prod = Productos.objects.get(pk=1)
    return render(request, 'eventos/nuevo.html', {'producto': prod})

