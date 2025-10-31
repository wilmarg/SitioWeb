from django.contrib import admin
from .models import *

# Register your models here.

class Categoria_Producto_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Categoria_Producto, Categoria_Producto_Admin)


class Producto_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Producto, Producto_Admin)
