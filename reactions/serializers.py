from rest_framework import serializers
from .models import Reaction

class ReactionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Reaction
        fields = "__all__"
        read_only_fields = ("user", "entry", "created_at")