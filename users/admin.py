from django.contrib import admin

from .models import User
from todos.models import Todo


class TodoInline(admin.StackedInline):
    model=Todo
    extra=0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """" Panel Admin for User Model. """
    date_hierarchy = "created_time"
    list_display = ['username', 'created_time']
    ordering = ['-created_time']
    inlines = [TodoInline]
