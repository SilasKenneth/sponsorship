from sponsorship.apps.authentication.users.user import User, Student
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student


class SponsorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sponsor
