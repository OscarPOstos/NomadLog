from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Reaction
from .serializers import ReactionSerializer
from entries.models import Entry

class ReactToEntryView(generics.CreateAPIView):
    serializer_class = ReactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        entry_id = self.kwargs["entry_id"]
        entry = Entry.objects.get(id=entry_id)

        existing = Reaction.objects.filter(entry=entry, user=request.user).first()
        if existing:
            return Response({"detail": "Ya reaccionaste a esta entrada."}, status=400)

        reaction = Reaction.objects.create(entry=entry, user=request.user)
        return Response(ReactionSerializer(reaction).data, status=201)


class EntryReactionCountView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, entry_id):
        count = Reaction.objects.filter(entry_id=entry_id).count()
        return Response({"entry": entry_id, "reactions": count})