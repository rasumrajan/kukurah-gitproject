# Generated by Django 3.0.7 on 2022-04-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0006_dog_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='Dogs_type',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Pups', 'Pups')], default='pups', max_length=6),
        ),
    ]