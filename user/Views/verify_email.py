import jwt
from rest_framework.response import Response
from ..models import MyUser as User
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def verify_email( request):

    token = request.data['token']

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        user = User.objects.get(id=payload['user_id'])
        if not user.is_verified:
            user.is_verified = True
            user.save()
        return Response({'message': 'Successfully activated'}, status=status.HTTP_200_OK)
    except jwt.ExpiredSignatureError as identifier:
        return Response({'message': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
    except jwt.exceptions.DecodeError as identifier:
        return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)