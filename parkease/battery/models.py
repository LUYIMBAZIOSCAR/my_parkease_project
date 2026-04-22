from django.db import models

# Create your models here.
class BatteryService(models.Model):

    SERVICE_CHOICES = [
        ('Hire', 'Hire'),
        ('Sale', 'Sale'),
    ]

    BATTERY_CHOICES = [
        ('N70', 'N70'),
        ('N50', 'N50'),
        ('Dry Cell', 'Dry Cell'),
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
            ('N70', 'Hire'): 20000,
            ('N70', 'Sale'): 180000,

            ('N50', 'Hire'): 15000,
            ('N50', 'Sale'): 150000,

            ('Dry Cell', 'Hire'): 10000,
            ('Dry Cell', 'Sale'): 80000,

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
