from django.shortcuts import render, HttpResponse
from .forms import *


# Create your views here.
def contacto(request):

    formulario = FormularioContacto()
    return render(request, "contacto/contacto.html", {'formulario':formulario})
