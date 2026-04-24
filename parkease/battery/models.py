from django.db import models

# Create your models here.
class BatteryService(models.Model):

    SERVICE_CHOICES = [
        ('Hire', 'Hire'),
        ('Sale', 'Sale'),
    ]

    BATTERY_CHOICES = [
        ('Car Battery', 'Car Battery'),
        ('Truck Battery', 'Truck Battery'),
    ]

    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    battery_type = models.CharField(max_length=30, choices=BATTERY_CHOICES)
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    amount = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        prices = {
            ('Car Battery', 'Hire'): 10000,
            ('Car Battery', 'Sale'): 80000,

            ('Truck Battery', 'Hire'): 30000,
            ('Truck Battery', 'Sale'): 300000,
        }

        self.amount = prices.get(
            (self.battery_type, self.service_type),
            0
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
