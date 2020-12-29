from .models import Author, Book, Library
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer, LibrarySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LibrarySerializer
