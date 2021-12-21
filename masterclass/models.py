from django.db import models
from margulan import settings


class Theme(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Заголовок")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Тема"
        ordering = ('title',)

    def __str__(self):
        return self.title


class Clas(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Куратор", related_name='class_created', on_delete=models.CASCADE)
    themes = models.ForeignKey(Theme, related_name='master', on_delete=models.CASCADE, verbose_name="Тема")
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Слог")
    image = models.FileField(upload_to='images', verbose_name="Изображение")
    video = models.URLField(verbose_name="Видео")
    overview = models.TextField(verbose_name="Обзор")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Мастер Класс"
        verbose_name_plural = "Мастер Класс"
        ordering = ('-created',)

    def __str__(self):
        return self.title
