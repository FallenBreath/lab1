from django.shortcuts import render
from django.http import HttpResponse
# request — это "письмо" от браузера с данными о пользователе

def home(request):
    return HttpResponse("<h1>Добро пожаловать в 3D Хранилище</h1><p>Система работает.</p>")
