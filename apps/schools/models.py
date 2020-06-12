from django.db import models


class School(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=40)


class Course(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id')

# Create your models here.
