# Generated by Django 3.1.2 on 2020-11-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20201109_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_organizer',
            field=models.BooleanField(default=False),
        ),
    ]
