from django.urls import path
from . import views

app_name="portafolio_app"

urlpatterns=[
    path('portafolio/',views.Portafolio.as_view(),name="portafolio"),
    path('cursosTomados/',views.CursoTomadoListView.as_view(),name="cursosTomados"),


    # ListView...

    path('proyectos/lista',views.ProyectoListView.as_view(),name="proyectos"),
    path('especializacion/lista/',views.EspecializacionListView.as_view(),name="especializacion-lista"),
    path('cursosImpartidos/lista/',views.CursoImpartidoListView.as_view(),name="cursosImpartidos-lista"),
    path('cursosTomados/lista/',views.CursoTomadoListView.as_view(),name="cursosTomados-lista"),

    # DetailView....

    path('proyecto/<pk>/detalle/',views.ProyectoDetailView.as_view(),name="proyecto-detail"),
    path('especializacion/<pk>/detalle/',views.EspecializacionDetailView.as_view(),name="especializacion-detail"),
    path('cursoImpartido/<pk>/detalle/',views.CursoImpartidoDetailView.as_view(),name="cursoImpartido-detail"),
    path('cursoTomado/<pk>/detalle/',views.CursoTomadoDetailView.as_view(),name="cursoTomado-detail"),


]