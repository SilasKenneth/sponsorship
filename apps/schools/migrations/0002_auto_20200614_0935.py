# Generated by Django 3.0.7 on 2020-06-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.UUIDField(default='cd686c6a-02c5-4ff6-bd9a-035653801215'),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_id',
            field=models.UUIDField(default='9c0d3feb-25cf-4a51-827c-21a4ec36a97e'),
        ),
    ]
