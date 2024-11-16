from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "get_equipments", "is_reserved_today")
    search_fields = ("name",)
    list_filter = ("equipments",)

    def get_equipments(self, obj):
        return ", ".join([equipment.name for equipment in obj.equipments.all()])
    get_equipments.short_description = "Equipments"

    def is_reserved_today(self, obj):
        today = now().date()
        return obj.reservations.filter(date=today).exists()
    is_reserved_today.short_description = "Reserved Today"
    is_reserved_today.boolean = True  # Zobrazí ikonu (✔/✖) místo True/False


class EquipmentAdmin(admin.ModelAdmin):
    """
    Display in table and values of Equipments in /admin/
    """
    list_display = ("name",)
    search_fields = ("name",)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("room", "date", "created_at")
    search_fields = ("room__name", "date")
    list_filter = ("room", "date")


admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Reservation, ReservationAdmin)