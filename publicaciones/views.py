from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "publicaciones/inicio.html")

def base (request):
    return render(request, "publicaciones/base.html")

def lista_publicaciones(request):
    publicaciones = [
        {"titulo": "Mi primera publicación", "autor": "Luciano Oscares"},
        {"titulo": "Mi segunda publicación", "autor": "Oriana Nahir"},
        {"titulo": "Mi Tercera publicación", "autor": "La moni"},
    ]
    contexto = {"publicaciones": publicaciones}
    return render(request, "publicaciones/lista_publicaciones", contexto)

def lista_autores(request):
    autores = [
        {"nombre": "Luciano", "posts": 3},
        {"nombre": "Oriana", "posts": 12},
        {"nombre": "Moni", "posts": 15},
    ]
    contexto = {"autores":autores}
    return render (request, "publicaciones/lista_autores.html", contexto)

def contacto (request):
    return render(request, "publicaciones/contacto.html")