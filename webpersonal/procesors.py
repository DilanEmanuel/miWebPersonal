from about_me.models import DatosAutor
from contacto.models import Apartado_Contacto,RedCotacto

def datos_autor(request):
    datosAutor=DatosAutor.objects.last()

    datosRetornar={
        'NOMBRE':"AUTOR ANONIMO",
        'OCUPACION':"OCUPACION ANONIMA",
        'CORREO':None,
        'NUMERO_TELEFONO':None,
    }
    if datosAutor:
        datosRetornar['NOMBRE']=datosAutor.nombre
        datosRetornar['OCUPACION']=datosAutor.ocupacion
        datosRetornar['CORREO']=datosAutor.correoElectronico
        datosRetornar['NUMERO_TELEFONO']=datosAutor.numeroTelefonico   
        
    return datosRetornar


def contexto_contactos(request):
    redesSociales=dict( ("CONTACTO_"+str(redSocial),redSocial.url) for redSocial in RedCotacto.objects.all() )
    return redesSociales



