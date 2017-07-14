from django import forms
from .models import Vuelo
from .models import Usuario
class ComprarVueloForm(forms.ModelForm):
	class Meta:
		model = Vuelo
		fields = ('lugar','nombreDeVuelo', 'horaYFechaDeEmbarque')
	