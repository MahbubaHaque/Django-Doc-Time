from django.db import models
from django.contrib.auth.models import User

from general_services.utils import encrypt, decrypt

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.name = encrypt(self.name)
        super(Medicine, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.get_name()
    
    def get_name(self):
        try:
            return decrypt(self.name)
        except:
            self.save()
            return decrypt(self.name)

class MedicalTest(models.Model):
    name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.name = encrypt(self.name)
        super(MedicalTest, self).save(*args, **kwargs)

    def get_name(self):
        try:
            return decrypt(self.name)
        except:
            self.save()
            return decrypt(self.name)

    def __str__(self):
        return self.get_name()

class Notification(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppointMent(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    appointment_time = models.DateField()
    age = models.IntegerField(default=0)
    contact_no = models.CharField(max_length=100, default='+880')
    def __str__(self):
        return f'{self.patient.username.upper()} has appoinment at {self.appointment_time}'


class PescribedMedicine(models.Model):
    comments = models.CharField(max_length=50000, null=True)
    appointment = models.ForeignKey(AppointMent, on_delete=models.CASCADE,null=True)
    medicine = models.ManyToManyField(Medicine,related_name='medicines',null=True)
    test = models.ManyToManyField(MedicalTest,related_name='tests',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.comments = encrypt(self.comments)
        super(PescribedMedicine, self).save(*args, **kwargs)
        
    # def __str__(self):
    #     return f"appoinment no {self.pk}"