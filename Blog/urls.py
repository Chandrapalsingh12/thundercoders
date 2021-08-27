from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('blogpost/<str:slug>', views.blog, name='Homes'),
    path('About/', views.about, name='About'),
    path('Contact/', views.contact, name='Contact'),
    path('allposts/', views.allpost, name='Contact'),
    path('signup/', views.signup, name='handelSignup'),
    path('login/', views.handelLogin, name='handelLogin'),
    path('logout/', views.handelLogout, name='handelLogin'),
    path('like/<int:pk>',views.Likeview, name='like_post')
    
]