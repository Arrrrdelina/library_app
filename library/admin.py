from django.contrib import admin
from .models import Author, Library, Book


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_of_book', 'nationality')
    list_display_links = ('name', 'name_of_book')
    search_fields = ('name', 'name_of_book')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name_of_book', 'libraries', 'pages')
    list_display_links = ('name_of_book', 'libraries')
    search_fields = ('name_of_book', 'libraries')


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('libraries', 'address', 'number')
    list_display_links = ('libraries', 'number')
    search_fields = ('libraries', 'number')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
