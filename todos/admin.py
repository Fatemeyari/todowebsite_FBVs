from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """ Admin panel for Todo model. """
    date_hierarchy = "created_time"
    list_display = ["title","get_username","created_time","done"]
    list_filter = ["done"]
    search_fields = ["title"]
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "username"
