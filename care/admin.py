from django.contrib import admin
from care.models import HealthcareFacility,Booking,Prescription

# Register your models here.
admin.site.register(HealthcareFacility)
admin.site.register(Booking)
admin.site.register(Prescription)
