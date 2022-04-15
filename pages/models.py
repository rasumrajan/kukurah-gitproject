from django.db import models
from django.utils import timezone
from datetime import timedelta

def one_month_from_today():
    return timezone.now() + timedelta(days=30)

# Create your models here.

#slider section
class dog_slider(models.Model):
    slider_name = models.CharField(max_length=225)
    slider = models.ImageField(upload_to='slider/%Y/%m/%d/')

    def __str__(self):
        return self.slider_name

#Our farm bread section
class Farm_bread(models.Model):
    bread_name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    age = models.DateField(default=one_month_from_today, blank=True, null=True)

    def __str__(self):
        return self.bread_name

