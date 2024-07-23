from django.shortcuts import render, HttpResponse
from . import models

def index(request):

    context = {
        "articles":
            models.Post.objects.all()
        
    }

    return render(request, 'index.html', context=context)

def article(request, id):
    context = {"article":models.Post.objects.get(pk=id)}
    return render(request, 'article.html', context=context)