from django.conf.urls import include, url
from . import views

urlpatterns = [
  	url(r'^$', views.inicio),
  	url(r'^inicio/', views.inicio),
    url(r'^vuelos/', views.lista_vuelos),
    url(r'^excursiones/', views.lista_excursiones),
    url(r'^hoteles/', views.lista_hoteles),
    url(r'^paquetes/', views.lista_paquetes),

    ]