from django.shortcuts import render, HttpResponse
from BlogApp.models import *


# Create your views here.
def blog(request):
    
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    
    categoria = Categorias.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    return render(request, "blog/categoria.html", {"categoria": categoria, "posts": posts})

