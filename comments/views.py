from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from entries.models import Entry

class EntryCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        entry_id = self.kwargs["entry_id"]
        return Comment.objects.filter(entry_id=entry_id)

    def perform_create(self, serializer):
        entry_id = self.kwargs["entry_id"]
        entry = Entry.objects.get(id=entry_id)
        serializer.save(user=self.request.user, entry=entry)