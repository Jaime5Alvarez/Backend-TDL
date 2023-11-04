from django.urls import path
from .Views.register_user import register_user
from .Views.verify_email import verify_email
from .Views.login_user import login_user
urlpatterns = [
    path('register/', register_user, name='register-user'),
   path('email-verify/', verify_email,name="email-verify"),
   path('login/', login_user, name="login-user")
    ]