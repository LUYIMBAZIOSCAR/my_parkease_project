from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    ROLE_CHOICES = [
        ('admin', 'System Admin'),
        ('attendant', 'Parking Attendant'),
        ('manager1', 'Tyre Section Manager'),
        ('manager2', 'Battery Section Manager'),
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='attendant',unique=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"