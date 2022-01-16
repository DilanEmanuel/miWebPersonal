from statistics import mode
from tabnanny import verbose
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.deletion import CASCADE
from about_me.functions import Apartado
from django.utils.timezone import now

# Create your models here.

class Proyecto(models.Model):
    
    imagen=models.ImageField(verbose_name="Imagen del proyecto",upload_to="fotosProyectos")
    titulo=models.CharField(max_length=100,verbose_name="Titulo del proyecto")
    terminoProyecto=models.DateField(verbose_name="Fecha de creacion del proyecto: ",default=now,null=True)
    

    prioridad=models.PositiveSmallIntegerField(verbose_name="Prioridad de aparicion",default=0)
    preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)

    descripccion=RichTextUploadingField(verbose_name="Descripccion del proyecto:",default="")


    # 'auto_now_add' añadira la hora a la cual se creado el modelo
    #fechaCreacion=models.DateTimeField(auto_now_add=True)

    # 'auto_now' modificara la hora cada vez que se actualice la instancia
    #fechaModificacion=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"

        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']

    def __str__(self):
        return "Proyecto: {}".format(self.titulo)


class Apartado_Portafolio(Apartado):
    proyectos=models.ManyToManyField(Proyecto)

    class Meta:
        verbose_name="Presentacion de la pagina del: portafolio"
        verbose_name_plural="Presentacion de la pagina del: portafolio"


class Logo(models.Model):
    nombre=models.CharField(verbose_name="Nombre:",max_length=150)
    imagen=models.ImageField(verbose_name="Imagen:",upload_to="fotosLogos")
    linkVista=models.URLField(verbose_name="Link:",max_length=200,null=True,blank=True)

    class Meta:
        verbose_name="Logo"
        verbose_name_plural="Logos"
    
    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    nombre=models.CharField(verbose_name="Nombre",max_length=100)

    class Meta:
        verbose_name="Habilidad"
        verbose_name_plural="Habilidades"

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre=models.CharField(verbose_name="Nombre: ",max_length=200)
    preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)

    empresaEmisora=models.ForeignKey(Logo,verbose_name="Empresa que emitio el curso",null=True,blank=True,on_delete=models.SET_NULL,related_name='cursos')
    logoExtra=models.ForeignKey(Logo,verbose_name="Logo secundario",null=True,blank=True,on_delete=models.SET_NULL,related_name='cursosLogoExtra')
    
    # limites...
    prioridad=models.PositiveSmallIntegerField(verbose_name="Prioridad de aparicion")
    urlCredencial=models.URLField(verbose_name="URL de la credencial",max_length=200,null=True,blank=True)
    idCredencial=models.CharField(verbose_name="ID de la credencial",max_length=200,null=True,blank=True)

    curriculum=models.FileField(verbose_name="PDF del certificado",upload_to="certificados",null=True,blank=True)
    descripccion=RichTextUploadingField(verbose_name="Descripccion: ",default="")
    urlAccesoCurso=models.URLField(verbose_name="URL de acceso al curso",max_length=200,null=True,blank=True)
    duracionHoras=models.PositiveSmallIntegerField(verbose_name="Duracion del curso en horas")


    def __str__(self):
        return "Curso: "+self.nombre


class CursoTomado(Curso):
    fechaExpedicion=models.DateField(verbose_name="Fecha de expedicion del curso ",default=now,null=False,blank=False)
    fechaCaducidad=models.DateField(verbose_name="Fecha de cadocidad(solo si tiene)",null=True,blank=True)
    habilidades=models.ManyToManyField(Habilidad,verbose_name="Habilidades que otorgan el curso:",related_name="get_cursos")

    class Meta:
        verbose_name="Curso tomado"
        verbose_name_plural="Cursos tomados"
        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']

class CursoImpartido(Curso):
    fechaInicio=models.DateField(verbose_name="Fecha de inicio del curso:",null=False,blank=False)
    fechaFinalizacion=models.DateField(verbose_name="Fecha de fin del curso(solo si tiene):",null=False,blank=False)


    class Meta:
        verbose_name="Curso impartido"
        verbose_name_plural="Cursos impartidos"
        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']

class Especilizacion(Curso):
    fechaExpedicion=models.DateField(verbose_name="Fecha de expedicion del curso: ",default=now,null=False,blank=False)
    fechaCaducidad=models.DateField(verbose_name="Fecha de cadocidad(solo si tiene):",default=now,null=True,blank=True)
    cursos=models.ManyToManyField(CursoTomado,through="EspecilizacionRelacion")
    totalCursos=models.PositiveSmallIntegerField(verbose_name="Numero de cursos de la especializacion:",default=0)

    class Meta:
        verbose_name="Especializacion tomada"
        verbose_name_plural="Especializaciones tomadas"
        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']


    def __str__(self):
        return "Especializacion: {}".format(self.nombre)



class EspecilizacionRelacion(models.Model):
    cursotomado=models.ForeignKey(Especilizacion,on_delete=models.CASCADE,verbose_name="Esepecializacion:",related_name="getCursosOrdenados")
    especilizacion=models.ForeignKey(CursoTomado,on_delete=models.CASCADE,verbose_name="Curso:")
    numeroCurso=models.PositiveSmallIntegerField(verbose_name="numero de curso")

    class Meta:
        verbose_name="Especializacion relacion curso"
        verbose_name_plural="Especializacion relacion curso"

    def __str__(self):
        return "Curso {} : {}".format(self.numeroCurso,self.especilizacion.nombre)

class ActividadRealizada(models.Model):
    descripccion=models.TextField(verbose_name="Descripccion de la actividad")

    class Meta:
        verbose_name="Actividad realizada"
        verbose_name_plural="Actividades realizadas"

    def __str__(self):
        return self.descripccion[:30]



class ExperienciaLaboral(models.Model):
    institucion=models.ForeignKey(Logo,on_delete=models.SET_NULL,null=True)
    actividades=models.ManyToManyField(ActividadRealizada)
    prioridad=models.PositiveSmallIntegerField(verbose_name="Prioridad de aparicion")
    fechaInicio=models.DateField(verbose_name="Fecha de inicio",null=False,blank=False)
    fechaFinalizacion=models.DateField(verbose_name="Fecha de fin",null=True,blank=True)
    

    class Meta:
        verbose_name="Experiencia laboral"
        verbose_name_plural="Experiencias laborales"
        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']        













    