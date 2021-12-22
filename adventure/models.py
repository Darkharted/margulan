from django.db import models

class Adventure(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Куратор", related_name='class_created', on_delete=models.CASCADE)
