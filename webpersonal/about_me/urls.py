from django.urls import path
from . import views


app_name="about_me_app"

urlpatterns=[
    path('',views.AboutMe.as_view(),name="about"),
    path('descargarCurriculum/',views.CurriculumDetail.as_view(),name="descargar-curriculum")
]