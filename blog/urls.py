from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.ShowArticleView.as_view(), name='article'),
    path('about', views.about, name='about'),
    path('create-article', views.CreateArticleView.as_view(), name='create-article'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.AuthenticationView.as_view(), name='login'),
    path('logout', views.accounts_logout, name='logout'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
]
