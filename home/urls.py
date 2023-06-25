from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('home/', home_page,name='home'),
    path('about/', about_page,name='about'),
    path('services/', services_page,name='services'),
    path('contact/', contact_page,name='contact'),
]