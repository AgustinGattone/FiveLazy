from django.shortcuts import render
from .models import Paquete
from .models import Vuelo



# Create your views here.
def lista_viaje(request):
    paquetesvar = Paquete.objects.get(nombre = 'Buenos Aires')
    return render(request, 'index.html', {'paquete': paquetesvar})

def listar_vuelos(request):
    vuelosvar = Vuelo.objects.all()
    return render(request, 'lista_viaje.html', {'vuelos': vuelosvar})

def mostrar_imagen(request):
    imagenvar = Paquete.objects.get(imagen = 'Argentina')
    return render (request, 'index.html', {'imagen': imagenvar})