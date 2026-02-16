from django.shortcuts import render, redirect # Добавляем redirect
from .models import Asset
from .forms import AssetForm # Импортируем нашу новую форму


# HttpResponse нам больше не нужен, render делает это за нас
def home(request):
    # all() возвращает хаос.
    # order_by('-created_at') сортирует по полю created_at.
    # Минус (-) означает "по убыванию" (DESC).
    assets = Asset.objects.all().order_by('-created_at')
    context_data = {
    'page_title': 'Главная Галерея',
    'assets': assets,
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

def upload(request):
    if request.method == 'POST':
        # Сценарий: Пользователь нажал "Отправить"
        form = AssetForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Если все поля заполнены верно - сохраняем в БД
            form.save()
            # И перекидываем пользователя на главную
            return redirect('home')
        else:
            # Если форма невалидна (например, неправильный файл)
            # Рендерим шаблон снова, но с формой, содержащей ошибки
            return render(request, 'gallery/upload.html', {'form': form})
    else:
        # Сценарий: Пользователь просто зашел на страницу (GET)
        form = AssetForm()  # Создаем пустую форму
        # Отдаем шаблон с пустой формой
        return render(request, 'gallery/upload.html', {'form': form})