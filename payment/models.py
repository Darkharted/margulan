from django.db import models


class Payment(models.Model):
    user = models.ForeignKey()