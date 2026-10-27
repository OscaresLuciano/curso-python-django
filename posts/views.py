from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'posts/inicio.html')

def nosotros(request):
    return HttpResponse("Esta es la seccion acerca de nosotros")