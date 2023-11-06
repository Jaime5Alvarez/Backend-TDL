from ..models import Todo
from rest_framework.response import Response
from rest_framework import status
from Utils.get_user_id import get_user_id
from ..serializer.Todoserializer import TodoSerializer
from rest_framework.decorators import api_view






@api_view(['GET'])
def GetTodos(request):
    user_id = get_user_id(request)
    todos = Todo.objects.filter(user=user_id)
    serializer = TodoSerializer(todos, many=True)
    print("hola")
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)
     
