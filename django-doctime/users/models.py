import uuid

from django.db import models
from django.contrib.auth.models import User


USER_CHOICES = (
    ('doctor','DOCTOR'),
    ('patient','PATIENT'),
    ('admin','ADMIN'),
)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, default='Medicine')
    location = models.CharField(max_length=255, default='Dhaka Medical college')
    user_type = models.CharField(max_length=50, choices=USER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.IntegerField(default=0)
    available = models.CharField(max_length=255, default='From 4 PM to 10 PM Sum, Mon , Wed, Friday')

    def __str__(self):
        return self.name
