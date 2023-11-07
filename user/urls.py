from django.urls import path
from .Views.register_user import register_user
from .Views.verify_email import verify_email
from .Views.login_user import login_user
from .Views.request_reset_password import RequestPasswordResetEmail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', register_user, name='register-user'),
   path('email-verify/', verify_email,name="email-verify"),
   path('login/', login_user, name="login-user"),
   path('reset-password/', RequestPasswordResetEmail, name="reset-password-email"),
    path('token/refresh/', 
        jwt_views.TokenRefreshView.as_view(), 
        name ='token_refresh')
    ]