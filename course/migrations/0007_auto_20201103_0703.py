# Generated by Django 3.0 on 2020-11-03 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20201102_1417'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set(),
        ),
    ]
