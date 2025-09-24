from django.shortcuts import render, HttpResponse

from ServiciosApp.models import Servicio

# Create your views here.

def home(request):
    return render(request, "SitioWebApp/home.html")

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, "SitioWebApp/servicios.html", {"servicios": servicios})


def tienda(request):
    return render(request, "SitioWebApp/tienda.html")

def blog(request):
    return render(request, "SitioWebApp/blog.html")

def contacto(request):
    return render(request, "SitioWebApp/contacto.html")

