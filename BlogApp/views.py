from django.shortcuts import render, HttpResponse
from BlogApp.models import *


# Create your views here.
def blog(request):
    
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

