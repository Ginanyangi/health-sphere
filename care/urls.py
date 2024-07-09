from django.urls import path
from care.views import HealthcareFacilityList, HealthCareFacilityDetail, BookingList, BookingDetail , PrescriptionListCreateView

urlpatterns = [
    path('facilities/', HealthcareFacilityList.as_view(), name='facility-list'),
    path('facilities/<int:pk>/', HealthCareFacilityDetail.as_view(), name='facility-detail'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('prescriptions/', PrescriptionListCreateView.as_view(), name='prescription-list-create'),
]

