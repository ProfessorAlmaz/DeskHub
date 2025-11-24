from django.contrib import admin

from coworkings.models import Room, Slot


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "city", "limit")
    list_filter = ("type",)
    search_fields = ("city",)

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "room_number", "room")
    search_fields = ("room__number",)