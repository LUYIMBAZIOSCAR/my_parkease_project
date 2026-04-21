from django.db import models

# Create your models here.
class TyreService(models.Model):
    SERVICE_CHOICES = [
        ('Pressure', 'Pressure'),
        ('Puncture', 'Puncture'),
        ('Valve', 'Valve'),
    ]
    SERVICE_PRICES = {
    'Pressure': 500,
    'Puncture': 5000,
    'Valve': 5000,
}
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    number_plate = models.CharField(max_length=10)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    amount = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
    Overrides the default save method to automatically assign 
    a price based on the selected service type before saving.
    """
        # Set the amount based on service_type; default to 0 if not found
        self.amount = self.SERVICE_PRICES.get(self.service_type, 0)
        # Call the 'real' save method from the parent class (Models) 
        # to actually commit the changes to the database
        super().save(*args, **kwargs)

    def __str__(self):
        """
    Returns a human-readable string representation of the object,
    useful for the Django Admin interface and debugging.
    """
        return f"{self.customer_name} - {self.service_type}"

