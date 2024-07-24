from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.article, name='article'),
    path('create-article', views.create_article, name='create-article'),

]
