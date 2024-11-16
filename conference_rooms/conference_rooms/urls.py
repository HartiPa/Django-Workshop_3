from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('reservation_system.urls')),
    path('admin/', admin.site.urls),
]
