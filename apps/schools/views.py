from rest_framework import generics, response, status
from apps.schools.serializers import SchoolSerializer, CourseSerializer
from rest_framework_simplejwt.models import TokenUser


class CreateSchoolAPIView(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def post(self, request, *args, **kwargs):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return respdjangoonse.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def get(self, request, *args, **kwargs):
        print(request.headers)
        return response.Response({})


class SchoolCoursesAPIView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        print(request)
        return response.Response({})

    def post(self, request, *args, **kwargs):
        print(dir(request))
        print(request.user.id)
        print(TokenUser)
        return response.Response({})
