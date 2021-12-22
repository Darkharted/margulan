from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ObjectDoesNotExist


class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Заголовок")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписка"
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_created', on_delete=models.CASCADE, verbose_name="Куратор")
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE, verbose_name="Подписка" )
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Заголовок")
    overview = models.TextField(verbose_name="Превью")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курс"
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE, )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE, )
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'video',
                                         'image',
                                         'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class BaseContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Text(BaseContent):
    body = models.TextField()


class ItemBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
