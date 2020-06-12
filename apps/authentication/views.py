from django.http import HttpResponse
from rest_framework import generics


class LoginView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        return HttpResponse()

# Create your views here.
