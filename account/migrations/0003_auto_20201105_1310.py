# Generated by Django 3.0 on 2020-11-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201105_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]