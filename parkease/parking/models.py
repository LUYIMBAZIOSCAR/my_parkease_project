

# Create your models here.
from django.db import models

class Vehicle(models.Model):
    VEHICLE_CHOICES = [
        ('Car', 'Car'),
        ('Motorcycle', 'Motorcycle'),
        ('Truck', 'Truck'),
    ]

    driver_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    number_plate = models.CharField(max_length=5)
    model = models.CharField(max_length=5)
    color = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    nin = models.CharField(max_length=14)

    entry_time = models.DateTimeField(auto_now_add=True)  # auto set
    exit_time = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.number_plate
