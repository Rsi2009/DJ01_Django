from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'caption':"CatDjango"})

def new(request):
    return render(request, 'main/new.html')

def page3(request):
    return render(request, 'main/page3.html')

def page4(request):
    return render(request, 'main/page4.html')

def data(request):
    return HttpResponse("<h1>Проект на Django создан 13 августа 2024 года</h1>")

def test(request):
    return HttpResponse("<h1>Тестируется проект на Django</h1>")

