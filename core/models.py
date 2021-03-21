from django.db import models


class Author(models.Model):
    name = models.CharField('Name', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Book(models.Model):
    name = models.CharField('Name', max_length=200)
    edition = models.IntegerField()
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
