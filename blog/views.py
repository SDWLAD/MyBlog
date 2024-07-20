from django.shortcuts import render, HttpResponse
from . import models

def index(request):

    context = {
        "articles":
            list(models.Post.objects.all())
        
    }

    return render(request, 'index.html', context=context)