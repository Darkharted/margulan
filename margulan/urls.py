from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article.views import CommentViewSet, ArticleViewset

router = DefaultRouter()
router.register('article', ArticleViewset)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include('user.urls')),
    path('api/v2/', include('video.urls')),
    path('api/v2/', include(router.urls)),

]
