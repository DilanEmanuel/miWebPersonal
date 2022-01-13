from django.contrib import admin
from .models import (Apartado_Portafolio,Proyecto,CursoImpartido,CursoTomado,
Especilizacion,EspecilizacionRelacion,Logo,ExperienciaLaboral,ActividadRealizada)

class ProyectoAdmin(admin.ModelAdmin):
    list_display=('prioridad','titulo','preparadoParaMostrar')

class CursoAmdin(admin.ModelAdmin):
    list_display=('prioridad','nombre','preparadoParaMostrar')

class ExperienciaAdmin(admin.ModelAdmin):
    list_display=('prioridad','institucion' )


admin.site.register(ExperienciaLaboral,ExperienciaAdmin)

admin.site.register(ActividadRealizada)

# Register your models here.
admin.site.register(Apartado_Portafolio)
#admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Proyecto,ProyectoAdmin)

admin.site.register(CursoImpartido,CursoAmdin)
admin.site.register(CursoTomado,CursoAmdin)
admin.site.register(Especilizacion,CursoAmdin)
admin.site.register(EspecilizacionRelacion)
admin.site.register(Logo)


