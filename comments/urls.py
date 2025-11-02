from django.urls import path
from .views import EntryCommentListCreateView

urlpatterns = [
    path("entries/<int:entry_id>/comments/", EntryCommentListCreateView.as_view(), name="entry-comments"),
]