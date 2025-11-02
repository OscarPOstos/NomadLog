from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/trips/', include('trips.urls')),
    path('api/', include('entries.urls')),
    path('api/', include('comments.urls')),
]