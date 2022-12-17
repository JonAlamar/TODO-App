from django.urls import path, include
from todoList import views

urlpatterns = [
    path('', views.index, name='view_todo'),
    path('update/<int:task_id>', views.update, name='update_todo'),
    path('add/', views.add, name='add_todo'),
    path('delete/<int:task_id>', views.delete, name='delete_todo'),
    path('search/', views.search, name='search_todo')
]