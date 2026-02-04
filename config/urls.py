from django.contrib import admin
from django.urls import path
# Импортируем нашу функцию из приложения gallery
from gallery.views import home, about

urlpatterns = [
path('admin/', admin.site.urls),# Пустая строка '' означает главную страницу сайта (http://localhost:8000/)
path('', home, name='home'),
 path('about/', about, name='about'),  # Маршрут для страницы "О проекте"
 
]
