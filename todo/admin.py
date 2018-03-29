from django.contrib import admin

from .models import Todo, UserTodo

admin.site.register(Todo)
admin.site.register(UserTodo)