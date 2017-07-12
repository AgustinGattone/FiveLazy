from django import forms
from .models import Vuelo
class VueloForm(forms.ModelForm):
	class Meta:
		model = Vuelo
		fields = ('lugar', 'horaYFechaDeEmbarque', 'precio', 'nombreDeVuelo')