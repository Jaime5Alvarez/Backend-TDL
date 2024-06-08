import requests
from google.auth.transport import requests
from google.oauth2 import id_token
from user.models import MyUser
from django.contrib.auth import authenticate
from django.conf import settings
from Utils.handleErrors import BadRequestException
from rest_framework_simplejwt.tokens import RefreshToken

class Google():
    @staticmethod
    def validate(access_token):
        try:
            id_info=id_token.verify_oauth2_token(access_token, requests.Request())
            if 'accounts.google.com' in id_info['iss']:
                return id_info
        except Exception:
            raise BadRequestException(errors={
					"message": "Error trying to sign in"
				})

def register_social_user(provider, email, first_name):
    old_user=MyUser.objects.filter(email=email)
    if old_user.exists():
        if provider == old_user[0].auth_provider:
            register_user=authenticate(email=email, password=settings.SOCIAL_AUTH_PASSWORD)

            refresh = RefreshToken.for_user(register_user)
            
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            raise BadRequestException(errors={
					"message": f"please continue your login with {old_user[0].auth_provider}"
				})
    else:
        new_user={
            'email':email,
            'first_name':first_name,
            'password':settings.SOCIAL_AUTH_PASSWORD
        }
        user=MyUser.objects.create_user(**new_user)
        user.auth_provider=provider
        user.is_verified=True
        user.save()
        login_user=authenticate(email=email, password=settings.SOCIAL_AUTH_PASSWORD)
       
        refresh = RefreshToken.for_user(login_user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }