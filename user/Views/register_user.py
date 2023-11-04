from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from ..models import MyUser as User
from ..serializer.CreateUserSerializer import CreateUserSerializer
from django.conf import settings
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from Utils.send_email import send_email
from django.conf import settings
@api_view(['POST'])
def register_user(request):
    # try:
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data['email'])
            token = RefreshToken.for_user(user).access_token
            Front_End_Url = settings.FRONTEND_URL
            relativeLink = reverse('email-verify')
            absurl = Front_End_Url + relativeLink + "?token=" + str(token)
            email_body = 'Hi ' + user.email + ' Use the link below to verify your email \n' + absurl
            data = {'to_email': user.email, 'email_subject': 'Verify your email', 'email_body': email_body}

            send_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # except Exception as e:
    #     return JsonResponse({"message": "server error"}, status=status.HTTP_400_BAD_REQUEST)
