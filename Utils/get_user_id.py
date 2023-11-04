 
import jwt
from django.conf import settings
def get_user_id(request):
    token = request.headers['Authorization'].split()[1]
    payload=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])

    return payload['user_id']