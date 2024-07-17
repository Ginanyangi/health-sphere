from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )

    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS =['full_name','phone_number','email']

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.user.username
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
