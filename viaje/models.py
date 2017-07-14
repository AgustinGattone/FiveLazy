from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    correoElectronico = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Vuelo(models.Model):
    nombreDeVuelo = models.CharField(max_length=200)
    lugar = models.ForeignKey('Destino')
    horaYFechaDeEmbarque = models.DateTimeField()
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='viaje/static/images')

    def __str__(self):
        return self.nombreDeVuelo



class Hotel(models.Model):
    nombre = models.CharField(max_length=200)
    lugar = models.ForeignKey('Destino')
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='viaje/static/images')

    def __str__(self):
        return self.nombre


class Excursion(models.Model):
    nombre = models.CharField(max_length=200)
    lugar = models.ForeignKey('Destino')
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nombre


class Paquete(models.Model):
    vuelo = models.ForeignKey('Vuelo')
    hotel = models.ForeignKey('Hotel')
    excursion = models.ForeignKey('Excursion')
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='viaje/static/images')

    def __str__(self):
        return self.nombre

class Destino(models.Model):
    destino = models.CharField(max_length=200)
    descripcionDelDestino = models.TextField()

    def __str__(self):
       return self.destino



       

class PaginaPrincipal(models.Model):
    imagen = models.ImageField(upload_to='viaje/static/images')
    paquete = models.ForeignKey('Paquete')

    def __str__(self):
       return self.imagen

        


