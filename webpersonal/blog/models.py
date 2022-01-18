from django.db import models
from model_utils.models import TimeStampedModel
from about_me.functions import Apartado
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(verbose_name="Nombre de la categoria",max_length=150)

    def __str__(self):
        return self.nombre

class ArticuloDeBlog(TimeStampedModel):
    titulo=models.CharField(verbose_name="Titulo",max_length=150)
    imagen=models.ImageField(verbose_name="Imagen de portada del articulo",upload_to="fotosPerfil")    
    preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)
    prioridad=models.PositiveSmallIntegerField(verbose_name="Prioridad de aparicion",default=0)
    categorias=models.ManyToManyField(Categoria,related_name="get_articulos")
    descripccion=models.TextField(verbose_name="Breve descripccion del articulo: ",default="",null=True)
    contenido=RichTextUploadingField(verbose_name="Contenido",default="")


    class Meta:
        verbose_name="Articulo de blog"
        verbose_name_plural="Articulos del blog"
        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad','modified']
        
    def __str__(self):
        return self.titulo[:30]

class Apartado_Blog(Apartado):
    articulosDestacados=models.ManyToManyField(ArticuloDeBlog)
    class Meta:
        verbose_name="Presentacion de la pagina principal del: Blog"
        verbose_name_plural="Presentacion de la pagina principal del: Blog"
 