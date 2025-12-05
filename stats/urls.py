from django.urls import path
from .views import PopularEntriesView, ActiveTravelersView

urlpatterns = [
    path("stats/popular/", PopularEntriesView.as_view(), name="stats-popular"),
    path("stats/active/", ActiveTravelersView.as_view(), name="stats-active"),
]