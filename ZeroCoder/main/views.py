from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def data(request):
    return HttpResponse("<h1>Проект на Django создан 13 августа 2024 года</h1>")

def test(request):
    return HttpResponse("<h1>Тестируется проект на Django</h1>")

