from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('base/', views.base, name='base'),
    path('publicaciones/lista_publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('lista_autores/', views.lista_autores, name='lista_autores'),
    path('contacto/', views.contacto, name='contacto'),
]