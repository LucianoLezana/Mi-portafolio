from django.contrib import admin
from django.urls import path
from WebLucianoApp import views


urlpatterns = [
   path('', views.Home, name='home'),
   path('about-me/', views.About, name='about_me'),
   path('project/', views.Project, name='project'),
   path('contact-me/', views.ContactMe, name='contact_me'),

]