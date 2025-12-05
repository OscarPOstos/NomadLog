from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Count
from django.db.models.functions import TruncMonth
from entries.models import Entry
from reactions.models import Reaction
from trips.models import Trip
from django.contrib.auth.models import User
from datetime import datetime

class PopularEntriesView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # Entradas ordenadas por cantidad de reacciones
        entries = (
            Entry.objects.annotate(total_reactions=Count("reactions"))
            .order_by("-total_reactions")[:10]
        )

        data = [
            {
                "id": entry.id,
                "title": entry.title,
                "trip": entry.trip.title,
                "author": entry.user.username,
                "reactions": entry.total_reactions,
            }
            for entry in entries
        ]

        return Response(data)


class ActiveTravelersView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        now = datetime.now()

        # Usuarios con más entradas creadas este mes
        users = (
            User.objects.annotate(
                entries_this_month=Count(
                    "entries",
                    filter=models.Q(
                        entries__created_at__year=now.year,
                        entries__created_at__month=now.month
                    )
                )
            )
            .order_by("-entries_this_month")
            .filter(entries_this_month__gt=0)[:10]
        )

        data = [
            {
                "user": user.username,
                "entries_this_month": user.entries_this_month,
            }
            for user in users
        ]

        return Response(data)
