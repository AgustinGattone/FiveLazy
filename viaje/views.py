from django.shortcuts import render
from .models import Paquete
from .models import Vuelo


# Create your views here.
def lista_viaje(request):
    paquetesvar = Paquete.objects.order_by('nombre')
    return render(request, '/home/informatica/Documentos/fivelazy/FiveLazy/viaje/templates/index.html', {'paquetes': paquetesvar})

def listar_vuelos(request):
    vuelosvar = Vuelo.objects.all()
    return render(request, 'viaje/lista_vuelos.html', {'vuelos': vuelosvar})
