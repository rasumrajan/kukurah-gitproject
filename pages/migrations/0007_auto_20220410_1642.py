# Generated by Django 3.0.7 on 2022-04-10 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_dog_slider_slider_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog_slider',
            old_name='dog_slider',
            new_name='slider',
        ),
    ]