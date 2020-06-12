from django.db import models
from apps.authentication.models.user import User
from apps.schools.models import Course


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    attached_account = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, db_column='course_id')
    phone = models.CharField(max_length=16)