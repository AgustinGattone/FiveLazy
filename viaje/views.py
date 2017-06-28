from django.shortcuts import render
from .models import Usuario


# Create your views here.
def lista_viaje(request):
    usuarios = Usuario.objects.order_by('nombre')
    return render(request, 'viaje/lista_viaje.html', {'usuarios': usuarios})
