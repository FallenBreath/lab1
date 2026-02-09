from django.contrib import admin
# Register your models here.

from .models import Asset # Импортируем наш класс
# Регистрируем
admin.site.register(Asset)