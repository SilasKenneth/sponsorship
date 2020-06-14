from django.db import models
import uuid


class School(models.Model):
    school_id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=40, null=False, default='No name')

    class Meta:
        db_table = 'schools'


class Course(models.Model):
    course_id = models.UUIDField(unique=True, auto_created=True, null=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, null=False, default='No name')
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id', to_field='school_id')

    class Meta:
        db_table = 'courses'

# Create your models here.
