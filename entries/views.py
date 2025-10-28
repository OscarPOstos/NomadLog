from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer
from trips.models import Trip

class TripEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        trip_id = self.kwargs["trip_id"]
        return Entry.objects.filter(trip_id=trip_id).order_by("-created_at")

    def perform_create(self, serializer):
        trip_id = self.kwargs["trip_id"]
        trip = Trip.objects.get(id=trip_id)
        serializer.save(user=self.request.user, trip=trip)


class EntryDetailView(generics.RetrieveDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        entry = self.get_object()
        if entry.user != request.user:
            return Response(
                {"error": "No tienes permiso para eliminar esta entrada."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().delete(request, *args, **kwargs)