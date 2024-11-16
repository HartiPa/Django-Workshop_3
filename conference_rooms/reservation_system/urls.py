from django.urls import path
from .views import rooms


urlpatterns = [
    path('', rooms, name='rooms'),
]