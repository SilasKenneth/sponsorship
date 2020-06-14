from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.authentication.managers.user import UserManager
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(unique=True, default=uuid.uuid4)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.CharField(
        max_length=3,
        choices=[('STD', 'Student'), ('STF', 'Staff'), ('SPN', 'Sponsor')],
        default='STD'
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'password']

    objects = UserManager()

    class Meta:
        db_table = 'users'


# Create your models here.
