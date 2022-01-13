from django.urls import path
from . import views

#app_name=""

urlpatterns=[
    path('portafolio/',views.Portafolio.as_view(),name="portafolio"),

]