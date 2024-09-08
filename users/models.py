from django.db import models
from django.contrib.auth.models import AbstractUser, User as DjangoUser


# Create your models here.

class DjangoUser(AbstractUser):
    pass

class Patient(models.Model):
    name = models.CharField(max_length=100, default=None)
    phone = models.BigIntegerField()
    related_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, related_name='patient_profile')
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    SPECIALITIES = [
        ('Allgemeinmedizin', 'Allgemeinmedizin'),
        ('Radiologie', 'Radiologie'),
        ('Hautarzt', 'Hautarzt'),
        ('Kinderarzt', 'Kinderarzt')
    ]
    TITLES = [
        ('Dr.', 'Dr.'),
        ('Prof Dr.', 'Prof Dr.'),
        ('Prof Dr. med', 'Prof Dr. med')
    ]
    name =  models.CharField(max_length=100, default=None)
    title = models.CharField(max_length=20, choices=TITLES, default='Dr.')
    speciality = models.CharField(max_length=20, choices=SPECIALITIES, default='Allgemeinmedizin')
    related_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, related_name='doctor_profile')
    
    def __str__(self):
        return f"{self.title} {self.name}"
    
    
class Appointment(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField()
    has_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    has_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        formatted_time = self.date.strftime('%d-%m-%Y at %H:%M')
        return f"On {formatted_time} - {self.has_patient.name} with {self.has_doctor.title} {self.has_doctor.name} for {self.title}"