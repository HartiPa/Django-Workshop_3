from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Rooms(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    equipments = models.ManyToManyField(Equipment, related_name="rooms", blank=True)

    def __str__(self):
        return f"{self.name} | {self.capacity} | {self.equipments}"


