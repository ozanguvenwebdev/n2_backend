from rest_framework.routers import DefaultRouter
from api.configurations.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'photos', PhotoViewSet, basename='photo')
router.register(r'todos', TodoViewSet, basename='todo')


urlpatterns = []

urlpatterns += router.urls

