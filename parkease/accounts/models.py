from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES=[('attendant','Parking Attendant'),
                  ('manager','Section Manager '),
                  ('admin','System Admin')]
    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    role= models.CharField(max_length=20,choices=ROLE_CHOICES)
    phone_number=models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.user.username


