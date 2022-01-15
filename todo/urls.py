from django.urls import path
from .views import index, updateTodo, deleteTodo

urlpatterns = [
    path('', index, name='home'),
    path('update_todo/<int:pk>/', updateTodo, name='update_todo'),
    path('delete/<int:pk>', deleteTodo, name='delete')
]