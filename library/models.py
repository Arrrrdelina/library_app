from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150)
    name_of_book = models.CharField(max_length=150)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.name_of_book, self.nationality


class Book(models.Model):
    name_of_book = models.CharField(max_length=150)
    libraries = models.CharField(max_length=150)
    pages = models.FloatField(max_length=3)

    def __str__(self):
        return self.name_of_book, self.libraries, self.pages


class Library(models.Model):
    libraries = models.CharField(max_length=150)
    address = models.TextField(max_length=200)
    number = models.FloatField(max_length=2)

    def __str__(self):
        return self.libraries, self.address, self.number
