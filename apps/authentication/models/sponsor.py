import uuid
from django.db import models

from apps.authentication.models.staff import User


class Sponsor(models.Model):
    sponsor_id = models.UUIDField(unique=True, default=uuid.uuid4)
    attached_account = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, unique=True)
    phone_number = models.CharField(max_length=16)
    approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'sponsors'
