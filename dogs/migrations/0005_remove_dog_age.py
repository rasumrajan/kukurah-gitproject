# Generated by Django 3.0.7 on 2022-04-13 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_auto_20220413_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='age',
        ),
    ]
