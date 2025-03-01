from django.contrib.auth.models import AbstractUser
from django.db import models


class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Car(models.Model):
    license_plate = models.CharField(max_length=15, null=True)
    make = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.make} {self.model}"


class DrivingLicense(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, null=True)
    document_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()

    def __str__(self):
        return f"{self.owner} ({self.license_number})"


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.owner} - {self.car}"


class CustomUser(AbstractUser):
    passport_number = models.CharField(max_length=20)
    home_address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.username
