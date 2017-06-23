from django.shortcuts import render

# Create your views here.
def lista_viaje(request):
	return render(request, 'viaje/lista_viaje.html', {})
