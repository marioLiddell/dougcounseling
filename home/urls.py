from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('locations/', views.locations, name='locations'),
    path('forms/', views.forms, name='forms'),
    path('learn/', views.learn, name='learn'),
]