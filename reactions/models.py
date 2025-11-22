from django.db import models
from django.contrib.auth.models import User
from entries.models import Entry

class Reaction(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("entry", "user")  # Un usuario solo reacciona una vez
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} → {self.entry.title}"