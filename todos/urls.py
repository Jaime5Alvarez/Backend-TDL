from django.urls import path
from .Views.get_todos import GetTodos

urlpatterns = [
    path('get-todos/', GetTodos, name='get-todos'),

    ]