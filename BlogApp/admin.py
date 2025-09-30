from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Categorias, CategoriaAdmin)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Post, PostAdmin)