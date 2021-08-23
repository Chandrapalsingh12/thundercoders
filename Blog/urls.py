from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('blogpost/<str:slug>', views.blog, name='Home'),
    path('About/', views.about, name='About'),
    path('Contact/', views.contact, name='Contact'),
    path('allposts/', views.allpost, name='Contact'),
    
]