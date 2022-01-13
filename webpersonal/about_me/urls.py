from django.urls import path
from . import views


#app_name=""

urlpatterns=[
    path('',views.AboutMe.as_view(),name="about"),
    path('descargarCurriculum/',views.CurriculumDetail.as_view(),name="descargar-curriculum")
]