from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),
    path('room/add/', add_room, name='add_room'),
    path('room/<int:room_id>/edit/', edit_room, name='edit_room'),
    path('room/<int:room_id>/book/', book_room, name='book_room'),
    path('room/<int:room_id>/delete/', delete_room, name='delete_room'),
]