from abc import ABC

from apps.authentication.models.staff import User
from apps.authentication.models.sponsor import Sponsor
from apps.authentication.models.student import Student
from apps.schools.models import Course
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = str(user.user_id)
        token['id'] = str(user.id)
        token['is_staff'] = user.is_staff
        token['is_sponsor'] = user.is_sponsor
        token['is_student'] = user.is_student

        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password']


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=123, required=True)
    password = serializers.CharField(write_only=True, required=True)
    fullnames = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    student_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Student
        fields = [
            'fullnames', 'username', 'email',
            'phone', 'course', 'birth_certificate',
            'national_id', 'student_id',
            'password']
        depth = 1


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
