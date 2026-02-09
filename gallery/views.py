from django.shortcuts import render
from .models import Asset # Импортируем модель, чтобы спрашивать данные

# HttpResponse нам больше не нужен, render делает это за нас
def home(request):
    # ORM Запрос: "Дай мне все объекты Asset из базы"
    assets = Asset.objects.all()
    context_data = {
    'page_title': 'Главная Галерея',
    'assets': assets, # Передаем реальный QuerySet (список)
    }
    return render(request, 'gallery/index.html', context_data)



def about(request):
    # Подготовка данных для шаблона
    context = {
        'page_title': 'О проекте - 3D Хранилище',
        'author_name': 'Ваше Имя',  # Замените на своё имя
        'course_name': 'Web Структуры',
        'project_description': 'Это учебный проект для хранения и управления 3D-моделями.',
        'technologies': [
            'Django 5.x',
            'Python 3.x',
            'HTML/CSS',
            'SQLite',
            'Django Templates'
        ],
        'current_year': 2024  # Можно динамически вычислять
    }
    
    return render(request, 'gallery/about.html', context)
