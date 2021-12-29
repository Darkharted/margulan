from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.enums import Choices
from model_utils.fields import StatusField
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()


class CreateDateModel(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


# модель статьи
class Article(CreateDateModel):
    STATUS = Choices('Available', 'Not existed')
    title = models.CharField("Заголовок", max_length=50, unique=True)
    description = models.TextField("Текст статьи")
    image = models.ImageField("Изображение",upload_to='media', null=False, blank=False)
    status = StatusField

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"

    def __str__(self):
        return self.title
    



# модель комментов
class Comment(CreateDateModel):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE,
        related_name='comment'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comment', null=True
    )
    text = models.TextField()




