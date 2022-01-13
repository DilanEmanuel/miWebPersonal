from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Apartado_Portafolio,Especilizacion,Proyecto,CursoImpartido,CursoTomado,ExperienciaLaboral


class Portafolio(TemplateView):
    template_name="portafolio/portafolio.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.last()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
            
            # solo retornara los 3 primeros proyectos
            context['proyectos']=Proyecto.objects.filter(preparadoParaMostrar=True)[:3]

            # solo retornara las 3 primeras especializaciones
            context['especializaciones']=Especilizacion.objects.filter(preparadoParaMostrar=True)[:3]

            # solo retornara los 3 primeros cursos impartidos
            context['cursosImpartidos']=CursoImpartido.objects.filter(preparadoParaMostrar=True)[:3]

            # solo retornara los primeros 6 cursos
            cursosTomados=list(CursoTomado.objects.filter(preparadoParaMostrar=True)[:6])
            cursosTomados=cursosTomados+cursosTomados+cursosTomados
            context['cursosTomados']=cursosTomados

            # retornara todo
            context['experienciaLaboral']=ExperienciaLaboral.objects.all()
            
        return context
