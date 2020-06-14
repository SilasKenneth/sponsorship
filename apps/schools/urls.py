from django.urls import path
from apps.schools.views import SchoolCoursesAPIView, CreateSchoolAPIView


urlpatterns = [
    path('<str:school_id>/courses/', SchoolCoursesAPIView.as_view()),
    path('', CreateSchoolAPIView.as_view())
]
