from django import forms
from .models import Vuelo
class ComprarVueloForm(forms.ModelForm):
	class Meta:
		model = Vuelo
		fields = ('lugar', 'horaYFechaDeEmbarque', 'precio', 'nombreDeVuelo')
	