from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^$', views.listar_productos, name="eventos.listado"),
      url(r'productos/nuevo/', views.nuevo, name="eventos.nuevo"),
  ]
