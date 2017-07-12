from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_vuelos),
    #url(r'^vuelo/(?P<pk>[0-9]+)/$', views.vuelo_detail),
    #url(r'^vuelo/nuevo/$', views.vuelo_nuevo, name='vuelo_nuevo'),
    ]