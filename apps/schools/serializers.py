from rest_framework import serializers
from apps.schools.models import Course, School


class CourseSerializer(serializers.ModelSerializer):

    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    course_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = Course
        fields = ['name', 'course_id', 'school']
        depth = 1


class SchoolSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = School
        fields = ['name', 'school_id']
