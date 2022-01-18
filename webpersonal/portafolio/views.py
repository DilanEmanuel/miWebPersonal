from ast import keyword
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Apartado_Portafolio,Habilidad,Especializacion,Proyecto,CursoImpartido,CursoTomado,ExperienciaLaboral



class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name="portafolio/detalle_proyecto.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
        return context

class EspecializacionDetailView(DetailView):
    model = Especializacion
    template_name="portafolio/detalle_especializacion.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
        return context

class CursoImpartidoDetailView(DetailView):
    model = CursoImpartido
    template_name="portafolio/detalle_cursoImpartido.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
        return context


class CursoTomadoDetailView(DetailView):
    model = CursoTomado
    template_name="portafolio/detalle_cursoTomado.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
        return context


class ProyectoListView(ListView):
    model = Proyecto
    template_name = "portafolio/lista_proyectos.html"
    paginate_by=6

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
            context['apartadoPortafolio']="Mis proyectos"
        return context


class EspecializacionListView(ListView):
    model =Especializacion
    template_name = "portafolio/lista_especializaciones.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
            context['apartadoPortafolio']="Mis especializaciones"
        return context


class CursoImpartidoListView(ListView):
    model = CursoImpartido
    template_name = "portafolio/lista_cursosImpartidos.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
            context['apartadoPortafolio']="Cursos impartidos"
        return context


class CursoTomadoListView(ListView):
    model = CursoTomado
    template_name = "portafolio/lista_cursosTomados.html"

    paginate_by=6



    def get_queryset(self):
        # un form manda unicamente el dato de: 'palabraClave'
        palabraClave=self.request.GET.get("palabraClave",None)
        
        # otro form manda unicamente el dato de: 'habilidad'
        id_habilidad=self.request.GET.get("habilidad",None)
        
        
        if palabraClave:
            cursosConDichaPalabra=CursoTomado.objects.filter(
                nombre__icontains=palabraClave
            )

            return cursosConDichaPalabra

        elif id_habilidad:
            try:
                id_habilidad=int(id_habilidad)
                habilidad=Habilidad.objects.get(id=id_habilidad)
                # haciendo uso del related name para hallar todos los cursos que pertenezcan a dicha categoria...
                cursosConDichaHabilidad=habilidad.get_cursos.all()
                return cursosConDichaHabilidad
            except:
                return CursoTomado.objects.none()
        else:
            datos=CursoTomado.objects.all()
            return datos




    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
            context['apartadoPortafolio']="Cursos tomados"

            # categorias
            context['habilidadesCursos']=Habilidad.objects.all()

           # solo retornara los primeros 6 cursos
            #cursosTomados=list(CursoTomado.objects.filter(preparadoParaMostrar=True)[:6])
            #cursosTomados=cursosTomados+cursosTomados+cursosTomados+cursosTomados+cursosTomados
            #context['cursotomado_list']=cursosTomados


        return context

            


class Portafolio(TemplateView):
    template_name="portafolio/portafolio.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Portafolio.objects.get_apartado()

        if datos:   
            context['imagenPortada']=datos.imagenPortada
            
            # solo retornara los 3 primeros proyectos
            context['proyectos']=Proyecto.objects.filter(preparadoParaMostrar=True)[:3]

            # solo retornara las 3 primeras especializaciones
            context['especializaciones']=Especializacion.objects.filter(preparadoParaMostrar=True)[:3]

            # solo retornara los 3 primeros cursos impartidos
            context['cursosImpartidos']=CursoImpartido.objects.filter(preparadoParaMostrar=True)[:3]

            # solo retornara los primeros 6 cursos
            cursosTomados=list(CursoTomado.objects.filter(preparadoParaMostrar=True)[:6])
            context['cursosTomados']=cursosTomados

            # retornara todo
            context['experienciaLaboral']=ExperienciaLaboral.objects.all()
            
        return context
