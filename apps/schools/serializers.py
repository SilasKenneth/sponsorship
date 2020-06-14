from rest_framework import serializers
from apps.schools.models import Course, School


class CourseSerializer(serializers.ModelSerializer):
    course_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)
    school = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'course_id']
        depth = 1


class SchoolSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(required=True)
    courses = serializers.SerializerMethodField()

    @property
    def get_courses(self):
        print(self.instance)
        return Course.objects.filter(school_id=self.instance)

    class Meta:
        model = School
        fields = ['name', 'school_id', 'courses']



