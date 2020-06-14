from django.db import models
from apps.authentication.models.sponsor import Sponsor
from apps.authentication.models.student import Student
from django.utils import timezone


class Sponsorship(models.Model):
    sponsor = models.ForeignKey(Sponsor, null=True, on_delete=models.SET_NULL, db_column='sponsor_id')
    date_created = models.DateTimeField(null=False, default=timezone.now)
    deadline = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'sponsorships'


class Application(models.Model):
    applicant = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, db_column='applicant_id')
    sponsorship = models.ForeignKey(Sponsorship, null=True, on_delete=models.SET_NULL, db_column='sponsorship_id')
    reasons = models.TextField(max_length=800, default='No reason')
    recommendation = models.FileField(null=True, max_length=255)

    class Meta:
        db_table = 'applications'
# Create your models here.
