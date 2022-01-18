from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView
from django.http import Http404
from .models import Apartado_Blog,ArticuloDeBlog,Categoria




class ArticuloDeBlogDetailView(DetailView):
    model = ArticuloDeBlog
    template_name = "blog/detalle_articuloBlog.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)        
        datosApartado=Apartado_Blog.objects.get_apartado()

        if datosApartado:   
            context['imagenPortada']=datosApartado.imagenPortada


        return context


class BlogPersonal(ListView):
    model = ArticuloDeBlog
    template_name = "blog/blog.html"
    paginate_by=6

    def get_queryset(self):

        # un form manda unicamente el dato de: 'palabraClave'
        palabraClave=self.request.GET.get("palabraClave",None)
        # otro form manda unicamente el dato de: 'habilidad'
        id_categoria=self.request.GET.get("categoria",None)
        
        
        if palabraClave:
            articulosConDichaPalabra=ArticuloDeBlog.objects.filter(
                titulo__icontains=palabraClave,preparadoParaMostrar=True
            ).order_by('created')

            return articulosConDichaPalabra

        elif id_categoria:
            try:
                id_habilidad=int(id_categoria)
                categoria=Categoria.objects.get(id=id_categoria)
                # haciendo uso del related name para hallar todos los cursos que pertenezcan a dicha categoria...
                articulosConDichaCategoria=categoria.get_articulos.all().filter(preparadoParaMostrar=True).order_by('created')
                return articulosConDichaCategoria
            except:
                return ArticuloDeBlog.objects.none()
        else:
            datos=ArticuloDeBlog.objects.all().filter(preparadoParaMostrar=True).order_by('created')
            return datos

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)        
        datosApartado=Apartado_Blog.objects.get_apartado()


        if datosApartado:   
            context['imagenPortada']=datosApartado.imagenPortada
            # solo retornara los primeros 3 de cada uno...
            context['articulosDestacados']=datosApartado.articulosDestacados.all().filter(preparadoParaMostrar=True).order_by('created')[:3]    
            context['articulosRecientes']=ArticuloDeBlog.objects.filter(preparadoParaMostrar=True).order_by('created')[:3]
            context['categorias']=Categoria.objects.all()

        return context


