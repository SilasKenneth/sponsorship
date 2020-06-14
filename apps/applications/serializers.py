from rest_framework import serializers
from apps.applications.models import Application, Sponsorship


class SponsorshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsorship
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
