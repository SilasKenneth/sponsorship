from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from apps.authentication.serializers import StudentSerializer
from apps.schools.models import Course
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
import uuid


class StudentCreateAccountView(CreateAPIView):

    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny, ]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(uuid.uuid4())
        if get_object_or_404(Course, course_id=serializer.data.get('course', uuid.uuid4())):
            return Response({})
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

