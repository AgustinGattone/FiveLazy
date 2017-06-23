from django.db import models
from django.utils import timezone


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    correoElectronico = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)


class Vuelo(models.Model):
    lugar = models.ForeignKey('Destino')
    horaYFechaDeEmbarque = models.DateTimeField(auto_now=False)
    precio = models.FloatField()
    nombreDeVuelo = models.CharField(max_length=200)


class Hotel(models.Model):
    nombre = models.CharField(max_length=200)
    lugar = models.ForeignKey('Destino')
    precio = models.FloatField()


class Excursion(models.Model):
    nombre = models.CharField(max_length=200)
    lugar = models.ForeignKey('Destino')
    precio = models.FloatField()


class Paquete(models.Model):
    vuelo = models.ForeignKey('Vuelo')
    hotel = models.ForeignKey('Hotel')
    excursion = models.ForeignKey('Excursion')
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()


class Destino(models.Model):
    destino = models.CharField(max_length=200)
