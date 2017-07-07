from django.shortcuts import render
from .models import Paquete
from .models import Vuelo


# Create your views here.
def lista_viaje(request):
    paquetesvar = Paquete.objects.order_by('nombre')
    return render(request, 'index.html', {'paquetes': paquetesvar})

def listar_vuelos(request):
    vuelosvar = Vuelo.objects.all()
    return render(request, 'lista_viaje.html', {'vuelos': vuelosvar})
