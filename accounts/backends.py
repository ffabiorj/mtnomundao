from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from .models import User

class ModelBackend(BaseModelBackend):
    """ create an authenticate base on by email"""
    
    def authenticate(self, request, username=None, password=None):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass