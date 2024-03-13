from django.shortcuts import render

def themes_list(request):
    with open('lessons.txt', 'r') as f:
        lessons = f.readlines()
    return render(request, 'themes_list.html', {'lessons': lessons})

from django.shortcuts import render

def themes_list(request):
    with open('lessons.txt', 'r') as f:
        lessons = f.readlines()
    return render(request, 'themes_list.html', {'lessons': lessons})

from django.urls import path
from . import views

urlpatterns = [
    path('themes/', views.themes_list, name='themes_list'),
]

