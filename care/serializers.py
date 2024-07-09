from rest_framework import serializers
from  care.models import HealthcareFacility, Booking , Prescription


class HealthcareFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareFacility
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'