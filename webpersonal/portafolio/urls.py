from django.urls import path
from . import views

app_name="portafolio_app"

urlpatterns=[
    path('portafolio/',views.Portafolio.as_view(),name="portafolio"),
    path('cursosTomados/',views.CursoTomadoListView.as_view(),name="cursosTomados"),
    path('proyectos/',views.ProyectoListView.as_view(),name="proyectos"),
    path('especializacion/lista/',views.EspecializacionListView.as_view(),name="especializacion-lista"),
    path('cursosImpartidos/lista/',views.CursoImpartidoListView.as_view(),name="cursosImpartidos-lista"),
    path('cursosTomados/lista/',views.CursoTomadoListView.as_view(),name="cursosTomados-lista"),



]