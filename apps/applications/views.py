from rest_framework import generics, response
from .permissions import StudentSubmitApplicationPermission, StaffCanDoAnythingToApplications
from .serializers import ApplicationSerializer


class CreateApplications(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (StudentSubmitApplicationPermission,)

    def post(self, request, *args, **kwargs):
        return response.Response({})


class ApplicationApproveAPIView(generics.UpdateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (StaffCanDoAnythingToApplications,)
# Create your views here.
