from django.conf import settings
from django.db import models
from user.models import CustomUser

class Adventure(models.Model):
    owner = models.ForeignKey(CustomUser, verbose_name="Куратор", related_name='owner_created', on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=50, unique=True)
    video = models.URLField(verbose_name="Видео")

    class Meta:
        verbose_name = "Путешестивие"
        verbose_name_plural = "Путешестивие"


class Event(models.Model):
    adventure = models.ForeignKey(Adventure,  on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятие"

class Date(models.Model):
    event_start = models.DateTimeField()
    event_end= models.DateTimeField()

    class Meta:
        verbose_name = "Старт"
        verbose_name_plural = "Старт"

class Ticket_Class(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    type= models.CharField(max_length=250)

    class Meta:
        verbose_name = "Билеты"
        verbose_name_plural = "Билеты"

class EventTicketSell(models.Model):
    event= models.ForeignKey(Event, on_delete=models.CASCADE)
    date= models.ForeignKey(Date, on_delete=models.CASCADE)
    ticket= models.ForeignKey(Ticket_Class, on_delete=models.CASCADE)
    max_sellable_tickets= models.IntegerField()

    class Meta:
        verbose_name = "Продажа билетов на мероприятие"
        verbose_name_plural = "Продажа билетов на мероприятие"