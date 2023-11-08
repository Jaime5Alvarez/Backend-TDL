from ..models import Todo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from ..serializer.Todoserializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated




@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def EditTodo(request, todo_uuid):
    try:
        todo = get_object_or_404(Todo, pk=todo_uuid)

        if todo is None:
            return Response({"message": "Todo not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Update the Todo instance with the new data
        todo.title = request.data['title']
        todo.date = request.data['date']
        todo.completed = request.data['completed']
        todo.save()

        # Serialize the updated Todo instance
        serializer = TodoSerializer(todo)

        return Response({"message": "Task Edited", "todo": serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
