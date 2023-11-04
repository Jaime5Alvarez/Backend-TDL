from rest_framework.decorators import api_view
from ..serializer.LoginSerializer import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

@api_view(['POST'])
def login_user(request):

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        tokens = serializer.validated_data['tokens']
        return Response(tokens, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


