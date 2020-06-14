import uuid
from django.db import models
from apps.authentication.models.staff import User
from apps.schools.models import Course


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    student_id = models.UUIDField(unique=True, default=uuid.uuid4())
    attached_account = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, db_column='course_id')
    phone = models.CharField(max_length=16)
    national_id = models.FileField(max_length=255, null=True)
    birth_certificate = models.FileField(max_length=255, null=True)
