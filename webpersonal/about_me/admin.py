from django.contrib import admin
from .models import DatosAutor,Apartado_AboutMe,Curriculum

from about_me.functions import ApartadoAdmin



# Register your models here.

admin.site.register(DatosAutor)
admin.site.register(Apartado_AboutMe,ApartadoAdmin)
admin.site.register(Curriculum)

