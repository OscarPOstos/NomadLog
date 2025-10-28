from django.urls import path
from .views import TripEntryListCreateView, EntryDetailView

urlpatterns = [
    path('trips/<int:trip_id>/entries/', TripEntryListCreateView.as_view(), name='trip-entries'),
    path('entries/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
]