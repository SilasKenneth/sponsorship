import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework_simplejwt import authentication


class JWTAuthentication(authentication.JWTTokenUserAuthentication):
    key = "Token"
