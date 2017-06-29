from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.lista_viaje),
        url(r'^vuelos/$', views.listar_vuelos),
    ]