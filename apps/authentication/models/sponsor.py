from django.db import models

from apps.authentication.models.user import User


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    attached_account = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, unique=True)
    phone_number = models.CharField(max_length=16)