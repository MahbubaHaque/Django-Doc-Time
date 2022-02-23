from django.db import models
from django.contrib.auth.models import User


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Notification(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppointMent(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    appointment_time = models.DateTimeField(auto_now_add=True)


class Pescription(models.Model):
    appointment = models.ForeignKey(AppointMent, on_delete=models.CASCADE)
    follow_up = models.DateTimeField(auto_now_add=True)


class PescribedMedicine(models.Model):
    pescription = models.ForeignKey(AppointMent, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine,related_name='medicines')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

