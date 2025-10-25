from django.shortcuts import render, redirect
from .forms import *
from django.conf import settings
from django.core.mail import send_mail, EmailMessage


# Create your views here.
'''
def contacto(request):

    formulario = FormularioContacto()

    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")


            #envio de correos con funcion 'send_mail'
            inf = formulario.cleaned_data
            send_mail(inf['nombre'], inf['contenido'], inf.get('email', ''), ['wilmar.galvisr29@gmail.com',])

            return redirect("/contacto?valido") 

    else: 
        formulario = FormularioContacto()

    return render(request, "contacto/contacto.html", {'formulario':formulario})

'''


def contacto(request):

    formulario = FormularioContacto()

    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            ## envío de correos con funcion 'email_message'
            email = EmailMessage("Mensaje recibido desde sitio web django",
                    "El usuario '{}' con dirección de correo '{}' escribe: \n\n {}".format(nombre, 
                            email, contenido), "", ['wilmar.galvisr29@gmail.com'], reply_to=[email])
            
            
            try:
                email.send()
                return redirect("/contacto?valido")
            except:
                return redirect("/contacto?novalido") 

    return render(request, "contacto/contacto.html", {'formulario':formulario})

