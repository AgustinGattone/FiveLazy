from django.conf.urls import include, url
from . import views

urlpatterns = [
  	url(r'^$', views.inicio),
  	url(r'^inicio/', views.inicio),
    url(r'^vuelos/', views.lista_vuelos, name="url.vuelos"),
    url(r'^excursiones/', views.lista_excursiones, name="views.lista_excursiones"),
    url(r'^hoteles/', views.lista_hoteles, name="views.lista_hoteles"),
    url(r'^paquetes/', views.lista_paquetes, name="views.lista_paquetes"),
    url(r'comprar/$', views.comprar, name='views.comprar'),

    ]