

# Create your models here.
from django.db import models
from django.utils import timezone

class Vehicle(models.Model):
    VEHICLE_CHOICES = [
        ('Car', 'Personal Car'),
        ('Motorcycle', 'Motorcycle'),
        ('Truck', 'Truck'),
        ('Taxi', 'Taxi'),
        ('Coaster','Coaster'),
        ('Boda', 'Boda-Boda'),
    ]

    driver_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    number_plate = models.CharField(max_length=10,unique=True)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    nin = models.CharField(max_length=14,unique=True)

    entry_time = models.DateTimeField(auto_now_add=True)  # auto set
    exit_time = models.DateTimeField(null=True, blank=True)

    is_parked = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.number_plate
    
    # A function for calculating the parking fees
    def calculate_fee(self):
        now=timezone.now()
        duration=now-self.entry_time
        seconds=duration.total_seconds()
        hours=seconds/3600

        # checking the duration is less than 3 hours
        if hours < 3:
            if self.vehicle_type=='Truck':
                return 2000
            elif self.vehicle_type in ['Car','Taxi']:
                return 2000
            elif self.vehicle_type=='Coaster':
                return 3000
            elif self.vehicle_type=='Boda':
                return 1000
            
            # checking whether it is day or night
            current_hour=now.hour
            # if it is day
            if 6 <= current_hour < 19:
                if self.vehicle_type=='Truck':
                    return 5000
                elif self.vehicle_type in ['Car','Taxi']:
                    return 3000
                elif self.vehicle_type=='Coaster':
                    return 4000
                elif self.vehicle_type=='Boda':
                    return 2000
            # if it is night
            else:
                if self.vehicle_type=='Truck':
                    return 10000
                elif self.vehicle_type in ['Car','Taxi']:
                    return 2000
                elif self.vehicle_type=='Coaster':
                    return 2000
                elif self.vehicle_type=='Boda':
                    return 2000

