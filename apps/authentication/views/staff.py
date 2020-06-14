from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentication.serializers import CustomTokenPairSerializer
from rest_framework import permissions


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer
    permission_classes = (permissions.AllowAny,)
