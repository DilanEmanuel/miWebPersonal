from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Apartado_Contacto, MensajeRecibido

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import FormularioContacto
from django.urls import reverse_lazy
from django.core.mail import send_mail
from webpersonal.settings import EMAIL_HOST_USER
from django.template import Template,RequestContext
import procesors
from about_me.models import DatosAutor
from .models import MensajeRecibido


# Create your views here.
class Contacto(TemplateView):
    template_name="contacto/contact.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Contacto.objects.last()

        if datos:      
            context['imagenPortada']=datos.imagenPortada
            context['incidicacionesContacto']=datos.indicacionesContacto
            context['numeroTelefonico']=datos.numeroTelefonico

        return context


# Create your views here.
class MensajeExito(TemplateView):
    template_name="contacto/exitoRegistro.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Contacto.objects.last()

        if datos:      
            context['imagenPortada']=datos.imagenPortada
            context['incidicacionesContacto']=datos.indicacionesContacto
            context['numeroTelefonico']=datos.numeroTelefonico

        return context
        

class FormularioContacto(FormView):
    template_name='contacto/contact.html'
    form_class=FormularioContacto
    success_url=reverse_lazy('contacto_app:mensajeContactoExito')
    #success_url="contact/exitoRegistro.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Contacto.objects.last()

        if datos:      
            context['imagenPortada']=datos.imagenPortada
            context['incidicacionesContacto']=datos.indicacionesContacto
            context['numeroTelefonico']=datos.numeroTelefonico

        return context

    def form_valid(self,form):
        nombre=self.request.POST.get('name')
        correo=self.request.POST.get('email')
        contenido=self.request.POST.get('content')

        # mensaje para el usuario 
        #autorSitioWeb=procesors.datos_autor.NOMBRE
        #autorSitioWeb=RequestContext(self.request,processors=[procesors.datos_autor]).get('NOMBRE')
        print("*****************************************")
        autorSitioWeb=DatosAutor.objects.last().nombre
        mensajeRecibido=MensajeRecibido.objects.last()

        asunto=mensajeRecibido.asunto
        mensaje="Hola: {}\n".format(nombre)
        mensaje+=mensajeRecibido.mensaje
        mensaje+="\n\nAtt: {}".format(autorSitioWeb)

        email_remitente=EMAIL_HOST_USER        
        # debe ser una lista por que se espera que el email de destino
        # pueda ser desde 1 email, hasta n emails.
        email_destino=[correo,]
        send_mail(asunto,mensaje,email_remitente,email_destino)

        # mensaje para el programador
        asunto="WEB personal, contacto:{}".format(nombre)
        mensaje="** Nombre del contacto:\n{}\n**Correo del contacto:\n{}\n**Mensaje:\n{}".format(nombre,correo,contenido)
        email_destino=[EMAIL_HOST_USER]
        send_mail(asunto,mensaje,email_remitente,email_destino)

        return super(FormularioContacto,self).form_valid(form)