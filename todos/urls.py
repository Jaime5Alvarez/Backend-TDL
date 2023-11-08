from django.urls import path
from .Views.get_todos import GetTodos
from .Views.add_todos import AddTodos
from .Views.edit_todo import EditTodo
from .Views.delete_todo import DeleteTodo

urlpatterns = [
    path('get-todos/', GetTodos, name='get-todos'),
    path('add-todos/', AddTodos, name='add-todos'),
    path('edit-todos/<uuid:todo_uuid>/', EditTodo, name='edit-todos'),
      path('delete-todos/<uuid:todo_uuid>/', DeleteTodo, name='delete-todos')

    ]