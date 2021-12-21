from django.db import models
from django.urls import reverse


class Package(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('package:product_detail', args=[self.id, self.slug])

    class Meta:
        verbose_name = "Пакет"
        verbose_name_plural = "Пакет"
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
