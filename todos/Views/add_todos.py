from ..models import Todo
from rest_framework.response import Response
from rest_framework import status
from Utils.get_user_id import get_user_id
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from user.models import MyUser
from ..serializer.Todoserializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated




@permission_classes([IsAuthenticated])
@api_view(['POST'])
def AddTodos(request):
    try:
        user = get_object_or_404(MyUser, pk=get_user_id(request))
        if user is None:
            return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        NewTodo = Todo.objects.create(
            user=user,
            title=request.data['title'],
            date=request.data['date'],
        )
        serializer = TodoSerializer(NewTodo)
        return Response({"message": "Task created", "todo":serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
