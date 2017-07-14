from django.contrib import admin

from .models import Destino
from .models import Vuelo
from .models import Hotel
from .models import Excursion
from .models import Paquete

# Register your models here.


admin.site.register(Vuelo)
admin.site.register(Hotel)
admin.site.register(Excursion)
admin.site.register(Paquete)
admin.site.register(Destino)
