from django.urls import path
from .Views.get_todos import GetTodos
from .Views.add_todos import AddTodos

urlpatterns = [
    path('get-todos/', GetTodos, name='get-todos'),
    path('add-todos/', AddTodos, name='add-todos'),

    ]