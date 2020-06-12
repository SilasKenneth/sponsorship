from django.contrib import admin
from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('sponsor/join/', admin.site.urls),
    path('createaccount/', admin.site.urls)
]