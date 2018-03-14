from django.contrib import admin
from django.urls import path
from django.conf.urls import url


from landing import views
urlpatterns = [
    path('landing/', views.landing, name='landing'),
   
]
