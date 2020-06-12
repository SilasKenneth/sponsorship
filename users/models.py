from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    names = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=512)
    role = models.CharField(
        max_length=3,
        choices=[('STD', 'Student'), ('STF', 'Staff'), ('SPN', 'Sponsor')],
        default='STD'
    )

    class Meta:
        pass


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    attached_account = models.ForeignKey(User, on_delete='CASCADE')
    course = models.ForeignKey(db_column='course_id')

    class Meta:
        pass


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    attached_account = models.ForeignKey(User, on_delete='CASCADE', unique=True)


# Create your models here.
