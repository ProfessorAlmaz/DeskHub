from django.db import models

class Room(models.Model):
    DESK = 'desk'
    MEETING_ROOM = 'meeting_room'
    TYPE_CHOICES = [(DESK, 'Рабочее место'), (MEETING_ROOM, 'Переговорная')]
    number = models.PositiveIntegerField()
    city = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    limit = models.IntegerField()
    def __str__(self):
        return "room " + str(self.number)

class Slot(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="slots")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


