from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from about_me.functions import Apartado

# Create your models here.

class Curriculum(models.Model):
    curriculum=models.FileField(verbose_name="Ingresa tu curriculum en formato pdf:",upload_to="Curriculum")


    def __str__(self):
        return "curriculum id:{}".format(self.id)

    class Meta:
        verbose_name="Curriculum"
        verbose_name_plural="Curriculums"


class Apartado_AboutMe(Apartado):
    fotoAutor=models.ImageField(verbose_name="Tu foto de perfil:",upload_to="fotosPerfil")    
    descripccionAutor=RichTextUploadingField(verbose_name="Descripccion tuya:",default="")

    class Meta:
        verbose_name="Presentacion de la pagina de: about_me"
        verbose_name_plural="Presentacion de la pagina de: about_me"

class DatosAutor(models.Model):
    nombre=models.CharField(max_length=150,verbose_name="Nombre:")
    ocupacion=models.CharField(max_length=150,verbose_name="Profesion:")
    fechaNacimiento=models.DateField(verbose_name="Fecha de nacimiento:")

    correoElectronico=models.EmailField(verbose_name="Correo electronico: ",null=True,default=None)
    numeroTelefonico=models.CharField(max_length=50,null=True,default=None)

    class Meta:
        verbose_name="Datos del autor"
        verbose_name_plural="Datos del autor"

    def __str__(self):
        return "{}-{}".format(self.id,self.nombre)


