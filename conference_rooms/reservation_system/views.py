from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
import calendar
from django.utils import timezone
from datetime import datetime


def home_page(request):
    rooms = Room.objects.all()
    today = timezone.now().date()
    # Vytvoříme seznam ID místností, které jsou dnes rezervované
    reserved_room_ids = [
        room.id for room in rooms if room.reservations.filter(today=today).exists()
    ]
    return render(request, 'home_page.html', {
        'rooms': rooms,
        'reserved_room_ids': reserved_room_ids
    })



def room_detail(request, room_id):
    """
    Displays room details along with future reservations.
    """
    room = get_object_or_404(Room, id=room_id)
    reservations = room.reservations.filter(date__gte=now().date())
    return render(request, 'room_detail.html', {'room': room, 'reservations': reservations})


def book_room(request, room_id):
    """
    Allows booking a room for a specific date, with validation for duplicate bookings and past dates.
    """
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        date = request.POST.get('date')

        # Validace:
        if date < str(now().date()):
            return render(request, 'book_room.html', {'room': room, 'error': "Cannot book past dates!"})

        # Validace: Duplicitní rezervace
        if room.reservations.filter(date=date).exists():
            return render(request, 'book_room.html', {'room': room, 'error': "Room is already booked for this date!"})

        # Create reservation
        Reservation.objects.create(room=room, date=date)
        return redirect('room_detail', room_id=room.id)

    reservations = room.reservations.filter(date__gte=now().date())
    return render(request, 'book_room.html', {'room': room, 'reservations': reservations})


def add_room(request):
    """
    Adds a new room with selected equipment.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        equipment_ids = request.POST.getlist('equipments')  # Získá zaškrtnuté vybavení
        room = Room.objects.create(name=name, capacity=capacity)
        room.equipments.set(equipment_ids)  # Nastaví vybavení pro místnost
        return redirect('home_page')
    equipments = Equipment.objects.all()
    return render(request, 'add_room.html', {'equipments': equipments})



def edit_room(request, room_id):
    """
    Edits an existing room and updates its equipment.
    """
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.name = request.POST.get('name')
        room.capacity = request.POST.get('capacity')
        equipment_ids = request.POST.getlist('equipments')  # Získá zaškrtnuté vybavení
        room.equipments.set(equipment_ids)  # Aktualizuje vybavení místnosti
        room.save()
        return redirect('home_page')
    equipments = Equipment.objects.all()
    return render(request, 'edit_room.html', {'room': room, 'equipments': equipments})


def delete_room(request, room_id):
    """
    Displays a confirmation page before deleting a room.
    If confirmed, deletes the room and redirects to the home page.
    """
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':  # Potvrzení od uživatele
        room.delete()
        messages.success(request, f"Room '{room.name}' has been successfully deleted.")
        return redirect('home_page')

    # Zobrazení potvrzovací stránky
    return render(request, 'confirm_delete.html', {'room': room})
