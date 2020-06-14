from django.db import models
import uuid


class School(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    school_id = models.UUIDField(default=str(uuid.uuid4()))
    name = models.CharField(max_length=40, null=False, default='No name')


class Course(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    course_id = models.UUIDField(default=str(uuid.uuid4()))
    name = models.CharField(max_length=200, null=False, default='No name')
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id')

# Create your models here.
