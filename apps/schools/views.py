from rest_framework import generics, response, status, permissions
from .serializers import SchoolSerializer, CourseSerializer
from .models import School, Course


class CreateSchoolAPIView(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def post(self, request, *args, **kwargs):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def get(self, request, *args, **kwargs):
        print(request.headers)
        return response.Response({})


class SchoolCoursesAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        school_id = kwargs.get('school_id')
        if school_id is None:
            return response.Response({'message': 'Invalid request'})
        school = School.objects.filter(school_id=school_id)
        if not school.count():
            return response.Response({'detail': 'The school you are looking for does not exist'})
        school = SchoolSerializer(school.first())
        return response.Response(school.data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        school_id = kwargs.get('school_id')
        if school_id is None:
            return response.Response({'message': 'Invalid request'})
        school = School.objects.filter(school_id=school_id)
        if not school.count():
            return response.Response({'detail': 'The school you are looking for does not exist'})
        data = request.data
        course = Course()
        course.school = school.first()
        course = CourseSerializer(course, data=data)
        if course.is_valid():
            course.save()
            return response.Response(course.data, status=status.HTTP_201_CREATED)
        return response.Response(course.errors, status=status.HTTP_400_BAD_REQUEST)
