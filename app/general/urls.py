from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('about_as/', views.AboutAsView, name='about_as'),
]

