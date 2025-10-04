from django.urls import path
from SitioWebApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name="Home"),
    path('tienda/', views.tienda, name="Tienda"),
    path('contacto/', views.contacto, name="Contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

