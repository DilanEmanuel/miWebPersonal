from django.contrib import admin
from .models import (Apartado_Portafolio,Habilidad,Proyecto,CursoImpartido,CursoTomado,
Especializacion,EspecializacionRelacion,Logo,ExperienciaLaboral,ActividadRealizada)
from about_me.functions import ApartadoAdmin

class EspecializacionRelacionAdmin(admin.ModelAdmin):

    list_display=(
         'nombre_Especializacion',
         'numeroCurso',
         'nombre_Curso',
         ) 

    def nombre_Especializacion(self,obj):
         return obj.cursotomado.nombre

    def nombre_Curso(self,obj):
         return obj.especializacion.nombre
          


class ProyectoAdmin(admin.ModelAdmin):
    list_display=('prioridad','titulo','preparadoParaMostrar')

class CursoAmdin(admin.ModelAdmin):
    list_display=('prioridad','nombre','preparadoParaMostrar')

class ExperienciaAdmin(admin.ModelAdmin):
    list_display=('prioridad','institucion' )


admin.site.register(ExperienciaLaboral,ExperienciaAdmin)

admin.site.register(ActividadRealizada)

# Register your models here.
admin.site.register(Apartado_Portafolio,ApartadoAdmin)
#admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Proyecto,ProyectoAdmin)

admin.site.register(Habilidad)

admin.site.register(CursoImpartido,CursoAmdin)
admin.site.register(CursoTomado,CursoAmdin)
admin.site.register(Especializacion,CursoAmdin)
admin.site.register(EspecializacionRelacion,EspecializacionRelacionAdmin)
admin.site.register(Logo)


