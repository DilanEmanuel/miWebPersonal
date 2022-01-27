from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Apartado_AboutMe,Curriculum
from django.http import HttpResponse,Http404, response
from django.http import FileResponse
import os



# Descargar curriculum: Solucion favorita...
class CurriculumDetail(View):
    # https://stackoverflow.com/questions/36392510/django-download-a-file

    def get(self, request, *args, **kwargs):
        miCurriculum = Curriculum.objects.last()

        if miCurriculum:
            filename=miCurriculum.curriculum.path
            
            if os.path.exists(filename):
                response = FileResponse(open(filename, 'rb'))
                return response
            raise Http404

        raise Http404


class CurriculumDetail_2(View):
    # https://stackoverflow.com/questions/36392510/django-download-a-file

    def get(self, request, *args, **kwargs):
        miCurriculum = Curriculum.objects.last()
        filename=miCurriculum.curriculum.path

        file_path =miCurriculum.curriculum.path   
        if os.path.exists(file_path):    
            with open(file_path, 'rb') as fh:   
                # tipos de content_type:  https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types 
                response = HttpResponse(fh.read(), content_type='application/pdf')    
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)    
                return response
        raise Http404

# Solucion para descargar curriculum por medio de link:
    #<li>
    #    <a class="btn btn-primary btn-sm"  style="font-size:15px;" href="/media/Curriculum/CV_DavidRoniHernandezBeltran.pdf" >Descargar CV</a>
    #</li>

    #<li>
    #    <a class="btn btn-primary btn-sm"  style="font-size:15px;" href="{{miCurriculum.url}} " >Descargar CV</a>
    #</li>



class AboutMe(TemplateView):
    template_name="about_me/about.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_AboutMe.objects.get_apartado()

        if datos:
            context['imagenPortada']=datos.imagenPortada
            context['descripccionAutor']=datos.descripccionAutor
            context['fotoAutor']=datos.fotoAutor
        return context