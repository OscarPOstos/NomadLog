from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"