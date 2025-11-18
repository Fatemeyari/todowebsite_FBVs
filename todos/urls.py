from django.urls import path

from .views import todo_list , todo_create ,is_done , todo_delete

urlpatterns = [
    path('list/', todo_list, name='todo_list'),
    path('create/' ,todo_create, name='todo_create' ),
    path('<int:pk>/', is_done, name='is_done'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
]