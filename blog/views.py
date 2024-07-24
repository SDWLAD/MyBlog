from django.shortcuts import render, HttpResponse, redirect
from . import models
from .forms import PostForm

def index(request):
    context = {
        "articles":
            models.Post.objects.all()
        
    }

    return render(request, 'index.html', context=context)

def article(request, id):
    context = {"article":models.Post.objects.get(pk=id)}
    return render(request, 'article.html', context=context)

def create_article(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'create_article.html', {'form': form})