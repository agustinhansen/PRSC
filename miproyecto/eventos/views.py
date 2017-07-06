from django.shortcuts import render
from .models import Productos

def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'eventos/productos.html', {'productos': productos})

def nuevo(request):
    return render(request, 'blog/nuevo.html', {'productos': productos})

