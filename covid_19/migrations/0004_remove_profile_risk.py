# Generated by Django 5.0 on 2024-05-07 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_19', '0003_profile_risk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='risk',
        ),
    ]
