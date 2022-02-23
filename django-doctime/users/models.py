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
    user_type = models.CharField(max_length=50, choices=USER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name