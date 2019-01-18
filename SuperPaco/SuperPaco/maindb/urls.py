"""SuperPaco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #Checking ID, and if non-existent, makes one (/back-end/id-check/)
    path('id_check/', views.id_check, name = 'id_check'),

    #Dumping unactive users to free up the server(/back-end/dump-start/)
    path('dump_start/', views.dumps, name = 'dumps'),

    #Basic user data(age, gender, q1, q2)
    path('basic_data/', views.basic_data, name="basic_data")

]
