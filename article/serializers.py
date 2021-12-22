from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    """
    Класс для перевода типов данных Python в json формат
    """

    class Meta:
        """
        Класс для передачи дополнительных данных
        """
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField("get_product_title")

    def get_article_title(self, article_comment):
        title = article_comment.article.title
        return title

    class Meta:
        model = Comment
        fields = "__all__"


    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        print(author)
        return Comment.objects.create(author=author, **validated_data)
