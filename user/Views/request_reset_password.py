
from ..models import MyUser as User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Utils.send_email import send_email
from rest_framework import status

@api_view(['POST'])
def RequestPasswordResetEmail(request):

    email = request.data.get('email', '')
    if  User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=['password'])       
        email_body = 'Hi '+user.email + \
        ' Your new password is  \n' + password + '\n you can change it in your profile  '
        data={ 'to_email': user.email,'email_subject': 'Reset your password', 'email_body': email_body}  
        send_email(data)
        return Response({'message': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


