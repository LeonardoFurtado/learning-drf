from .models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
        )


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'edition',
            'publication_year',
            'authors',
        )
