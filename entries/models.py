from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

class Entry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="entries")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="entries/photos/", blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.trip.title}) - {self.user.username}"