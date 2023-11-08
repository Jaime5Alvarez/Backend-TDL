from ..models import Todo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from ..serializer.Todoserializer import TodoSerializer

@api_view(['DELETE'])
def DeleteTodo(request, todo_uuid):
    try:
        todo = get_object_or_404(Todo, pk=todo_uuid)

        if todo is None:
            return Response({"message": "Todo not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the Todo instance with the new data
        todo.delete()

     

        return Response({"message": "Task deleted"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
