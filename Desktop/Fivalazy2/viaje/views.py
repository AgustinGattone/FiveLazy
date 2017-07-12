from django.shortcuts import render
from .models import Vuelo
#from .forms import VueloForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def lista_vuelos(request):
	vuelosvar = Vuelo.objects.all()
	return render(request, 'viaje/lista_vuelos.html', {'vuelos': vuelosvar})

def vuelo_detail (request, pk):
	vuelosvar = get_object_or_404(Vuelo, pk=pk)
	return render(request, 'viaje/vuelo_detail.html', {'vuelos': vuelosvar})