from django.db import models


class Author(models.Model):
    name = models.CharField('Name', max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Name', max_legth=200)
    edition = models.IntegerField()
    publication_year = models.DateField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
