from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, redirect
from . import models
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    paginate_by = 9
    model = models.Post
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return models.Post.objects.order_by('-created_at')

class ShowArticleView(CreateView):
    form_class = CommentForm
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['article'] = models.Post.objects.get(id=self.kwargs['pk'])
        context['comments'] = models.Comment.objects.filter(post=self.kwargs['pk']).order_by('-created_at')
        context['form'] = CommentForm()
        context['article'].views_count += 1
        context['article'].save()


        return context
    
    def form_valid(self, form):
        try:
            form.instance.post = models.Post.objects.get(id=self.kwargs['pk'])
            form.instance.author = self.request.user
            return super().form_valid(form)
        except:
            return self.form_invalid(form)

class CreateArticleView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'create_article.html'
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    

class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/", args=(),kwargs={})

class ProfileView(LoginRequiredMixin, DetailView):
    model = models.User
    template_name = 'profile.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = models.Post.objects.filter(author=self.kwargs['pk']).order_by('-created_at')
        context['articles'] = articles[:9]

        now = timezone.now()
        start_date = now - timedelta(days=15)
        activity = {'x': [], 'y': []}
        for i in range(16):
            day = start_date + timedelta(days=i)
            day_str = day.strftime('%Y-%m-%d')
            activity['x'].append(day_str)
            
            count = articles.filter(created_at__date=day.date()).count()
            activity['y'].append(count)
            context['activity'] = activity
        return context

class AuthenticationView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'
    def get_success_url(self):
        return "/"

def accounts_logout(request):
    logout(request)
    return redirect("/", args=(),kwargs={}) 

def about(request):
    return render(request, 'about.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')