import uuid
from django.db import models

from apps.authentication.models.staff import User


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    sponsor_id = models.UUIDField(unique=True, default=uuid.uuid4())
    attached_account = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, unique=True)
    phone_number = models.CharField(max_length=16)