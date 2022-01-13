from about_me.models import DatosAutor
from contacto.models import Apartado_Contacto,RedCotacto

def datos_autor(request):
    datosAutor=DatosAutor.objects.last()

    datosRetornar={
        'NOMBRE':"AUTOR ANONIMO",
        'OCUPACION':"OCUPACION ANONIMA"
    }
    if datosAutor:
        datosRetornar['NOMBRE']=datosAutor.nombre
        datosRetornar['OCUPACION']=datosAutor.ocupacion
        
    return datosRetornar


def contexto_contactos(request):
    redesSociales=dict( ("CONTACTO_"+str(redSocial),redSocial.url) for redSocial in RedCotacto.objects.all() )
    return redesSociales



def datos_contacto(request):
    datosContacto=Apartado_Contacto.objects.last()
    datosRetornar={
        'CORREO':None,
        'NUMERO_TELEFONO':None,
    }
    if datosContacto:
        datosRetornar['CORREO']=datosContacto.correo
        datosRetornar['NUMERO_TELEFONO']=datosContacto.numeroTelefonico      
    return datosRetornar
