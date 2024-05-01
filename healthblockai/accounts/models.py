from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    health_insurance = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    medical_license_number = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    clinic_hospital_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
