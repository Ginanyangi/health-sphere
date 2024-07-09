from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics , permissions
from care.models import HealthcareFacility, Booking , Prescription
from care.serializers import HealthcareFacilitySerializer, BookingSerializer , PrescriptionSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.

class HealthcareFacilityList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        facilities = HealthcareFacility.objects.all()
        serializer = HealthcareFacilitySerializer(facilities, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.permission_classes = [permissions.IsAuthenticated]
        serializer = HealthcareFacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class HealthCareFacilityDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return HealthcareFacility.objects.get(pk=pk)
        except HealthcareFacility.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        facility = self.get_object(pk)
        serializer = HealthcareFacilitySerializer(facility)
        return Response(serializer.data)

    def put(self, request, pk):
        facility = self.get_object(pk)
        serializer = HealthcareFacilitySerializer(facility, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        facility = self.get_object(pk)
        facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BookingList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookingDetail(APIView):
    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, pk):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = self.get_object(pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PrescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prescription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)