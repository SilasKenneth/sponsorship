from django.urls import path
from .views import CreateApplications

urlpatterns = [
    path('submit/', CreateApplications.as_view()),
    path('<application_id>/approve/', CreateApplications.as_view()),
    path('<application_id>/accept/', CreateApplications.as_view()),
]
