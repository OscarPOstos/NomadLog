from rest_framework import generics, permissions
from .models import Trip
from .serializers import TripSerializer

class TripListCreateView(generics.ListCreateAPIView):
    queryset = Trip.objects.filter(is_public=True).order_by("-created_at")
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TripDetailView(generics.RetrieveDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        trip = self.get_object()
        if trip.user != request.user:
            from rest_framework.response import Response
            from rest_framework import status
            return Response({"error": "No tienes permiso para eliminar este viaje."}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)