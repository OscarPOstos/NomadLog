from django.urls import path
from .views import ReactToEntryView, EntryReactionCountView

urlpatterns = [
    path("entries/<int:entry_id>/react/", ReactToEntryView.as_view(), name="react-entry"),
    path("entries/<int:entry_id>/reactions/", EntryReactionCountView.as_view(), name="entry-reactions"),
]
