from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    trip_title = serializers.ReadOnlyField(source="trip.title")

    class Meta:
        model = Entry
        fields = "__all__"
        read_only_fields = ("user", "trip", "created_at")