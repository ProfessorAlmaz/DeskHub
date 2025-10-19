from django.contrib import admin

from coworkings.models import Room, Slot


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "city", "limit")
    list_filter = ("city",)
    search_fields = ("number",)

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "room__number")
    search_fields = ("room__number",)