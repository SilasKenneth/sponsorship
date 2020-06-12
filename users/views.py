from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):

    def get(self, request, *args, **kwargs):
        print(request, dir(request))
        return HttpResponse()

# Create your views here.
