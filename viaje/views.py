from django.shortcuts import render
from .models import Vuelo
from .models import Excursion
from .models import Hotel
from .models import Paquete
from .forms import ComprarVueloForm

# Create your views here.
def lista_vuelos(request):
	vuelosvar = Vuelo.objects.all()
	return render(request, 'viaje/lista_vuelos.html', {'vuelos': vuelosvar})

def lista_excursiones(request):
	excursionesvar = Excursion.objects.all()
	return render(request, 'viaje/lista_excursiones.html', {'excursiones': excursionesvar})

def lista_hoteles(request):
	hotelesvar = Hotel.objects.all()
	return render(request, 'viaje/lista_hoteles.html', {'hoteles': hotelesvar})

def lista_paquetes(request):
	paquetesvar = Paquete.objects.all()
	return render(request, 'viaje/lista_paquetes.html', {'paquetes': paquetesvar})


def inicio(request):
    iniciovar = Paquete.objects.all()
    return render (request, 'viaje/inicio.html', {'paquetes': iniciovar})


def comprar(request):
	form = ComprarVueloForm()
	return render (request, 'viaje/comprar.html', {'forms': form})
