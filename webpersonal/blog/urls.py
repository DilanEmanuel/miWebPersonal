from django.urls import path
from . import views


app_name="blog_app"

urlpatterns = [
    path('blogPersonal/inicio',views.BlogPersonal.as_view(),name='blog-inicio'),
    path('blogPersonal/<pk>/articulo',views.ArticuloDeBlogDetailView.as_view(),name='blog-articuloDetail')
    
]