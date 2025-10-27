from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Trip
        fields = "__all__"
        read_only_fields = ("user", "created_at")