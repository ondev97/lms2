# Generated by Django 3.0 on 2020-11-03 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201024_0756'),
        ('course', '0008_enrollment_student'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('course', 'student')},
        ),
    ]