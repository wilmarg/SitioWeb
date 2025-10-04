from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "SitioWebApp/home.html")

def tienda(request):
    return render(request, "SitioWebApp/tienda.html")

def contacto(request):
    return render(request, "SitioWebApp/contacto.html")

