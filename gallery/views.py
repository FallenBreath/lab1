from django.shortcuts import render
# HttpResponse нам больше не нужен, render делает это за нас
def home(request):
    # 1. Готовим данные (Context). Это словарь Python.
    # Имитация данных из базы (список словарей)
    fake_database = [
    {'id': 1, 'name': 'Sci-Fi Helmet', 'file_size': '15 MB'},
    {'id': 2, 'name': 'Old Chair', 'file_size': '2 MB'},
    {'id': 3, 'name': 'Cyber Truck', 'file_size': '10 MB'},
    {'id': 4, 'name': 'green labubu', 'file_size': '12 MB'},
    ]
    context_data = {
    'page_title': 'Главная Галерея',
    'assets': fake_database, # Передаем весь список
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
