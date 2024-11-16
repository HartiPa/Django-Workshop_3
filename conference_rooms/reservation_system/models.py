from django.db import models
from django.utils.timezone import now


class Equipment(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()
    equipments = models.ManyToManyField(Equipment, related_name="rooms", blank=True)

    def __str__(self):
        return f"{self.name} | {self.capacity} | {', '.join(e.name for e in self.equipments.all())}"


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.room.name} on {self.date}"

    class Meta:
        unique_together = ('room', 'date')
