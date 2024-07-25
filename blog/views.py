from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from . import models
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView

class IndexView(ListView):
    model = models.Post
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return models.Post.objects.order_by('-created_at')

class ShowArticleView(DetailView):
    model = models.Post
    template_name = 'article.html'
    context_object_name = 'article'

class CreateArticleView(CreateView):
    form_class = PostForm
    template_name = 'create_article.html'