from rest_framework import routers
from .api import AuthorViewSet, BookViewSet, LibraryViewSet


router = routers.DefaultRouter()
router.register('api/library', AuthorViewSet, 'author')
router.register('api/library', BookViewSet, 'book')
router.register('api/library', LibraryViewSet, 'library')

urlpatterns = router.urls
