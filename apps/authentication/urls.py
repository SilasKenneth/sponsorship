from django.urls import path
from rest_framework_simplejwt.views import (
    TokenVerifyView, TokenRefreshView
)
from django.conf.urls.static import static
from django.conf import settings
from apps.authentication.views.sponsor import SponsorCreateAccountView
from apps.authentication.views.student import StudentCreateAccountView
from apps.authentication.views.staff import CustomTokenObtainView

urlpatterns = [
    path('token/', CustomTokenObtainView.as_view()),
    path('sponsor/join/',  SponsorCreateAccountView.as_view()),
    path('student/register/',  StudentCreateAccountView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('token/verify', TokenVerifyView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)