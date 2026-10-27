from django.db import models
from django.http import HttpResponse
from django.shortcuts import render

# Create your models here.
def inicio(request):
    return HttpResponse("Bienvenidos al blog")