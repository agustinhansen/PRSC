from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^$', views.listar_productos),
      url(r'^productos/(?P<pk>[0-9]+)/$', views.nuevo),
  ]
