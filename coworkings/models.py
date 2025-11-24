from django.db import models
from django.contrib.auth.models import AbstractUser as UserModel

class Room(models.Model):
    DESK = 'desk'
    MEETING_ROOM = 'meeting_room'
    TYPE_CHOICES = [(DESK, 'Рабочее место'), (MEETING_ROOM, 'Переговорная')]
    number = models.PositiveIntegerField(verbose_name='Номер комнаты')
    city = models.CharField(max_length=30, verbose_name='Город')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Тип')
    limit = models.IntegerField(verbose_name='Лимит')
    def __str__(self):
        return "Комната " + str(self.number)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

class Slot(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="Слот")
    start_time = models.DateTimeField(verbose_name='Время начала')
    end_time = models.DateTimeField(verbose_name='Время конца')

    class Meta:
        verbose_name = 'Слот'
        verbose_name_plural = 'Слоты'

class User(UserModel):
    fullname = models.CharField(verbose_name='Имя и фамилия')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'