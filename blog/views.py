from django.forms import BaseModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
from . import models
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login

class IndexView(ListView):
    paginate_by = 9
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

class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/", args=(),kwargs={})


class AuthenticationView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'
    def get_success_url(self):
        return "/"

def accounts_logout(request):
    logout(request)
    return redirect("/", args=(),kwargs={}) 