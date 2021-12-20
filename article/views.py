from rest_framework import viewsets
from article.serializers import CommentSerializer, ArticleSerializer
from .models import Article, Comment
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    queryset = Article.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter
    ]
    filter_fields = ['title']
    search_fields = ['title', 'id']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticatedOrReadOnly()]
        return []


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

