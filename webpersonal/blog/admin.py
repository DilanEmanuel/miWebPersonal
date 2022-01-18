from django.contrib import admin
from .models import ArticuloDeBlog,Categoria,Apartado_Blog
from about_me.functions import ApartadoAdmin


class ArticuloDeBlogAdmin(admin.ModelAdmin):
    list_display=('prioridad','titulo','created','preparadoParaMostrar',)
    readonly_fields=(
        'created',
        'modified',
    )

    # ordenando del mas reciente al menos reciente
    ordering=('prioridad','created')




# Register your models here.
admin.site.register(Apartado_Blog,ApartadoAdmin)
admin.site.register(ArticuloDeBlog,ArticuloDeBlogAdmin)
admin.site.register(Categoria)
