from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.ShowArticleView.as_view(), name='article'),
    path('create-article', views.CreateArticleView.as_view(), name='create-article'),

]
