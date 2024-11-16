from django.contrib import admin
from .models import *


class RoomsAdmin(admin.ModelAdmin):
    """
    Display in table and values of Rooms in /admin/
    """
    list_display = ("name", "capacity", "get_equipments")
    search_fields = ("name",)
    list_filter = ("equipments",)

    def get_equipments(self, obj):
        return ", ".join([equipment.name for equipment in obj.equipments.all()])
    get_equipments.short_description = "Equipments"


class EquipmentAdmin(admin.ModelAdmin):
    """
    Display in table and values of Equipments in /admin/
    """
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Equipment, EquipmentAdmin)