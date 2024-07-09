from django.db import models
from accounts.models import CustomUser

# Create your models here.

class HealthcareFacility(models.Model):
    FACILITY_TYPES = [
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('pharmacy', 'Pharmacy'),
        ('ambulance', 'Ambulance'),
    ]

    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    facility_type = models.CharField(max_length=10, choices=FACILITY_TYPES)
    is_open_24_7 = models.BooleanField(default=False)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    facility = models.ForeignKey(HealthcareFacility, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.facility} - {self.appointment_time}'


class Prescription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(
        HealthcareFacility,
        on_delete=models.CASCADE,
        limit_choices_to={'facility_type': 'pharmacy'}
    )
    prescription_details = models.TextField()
    date_issued = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Prescription for {self.user.username} at {self.pharmacy.name}'