from rest_framework import serializers
from bookstore.models import Book, Writer

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'book_name',
            'writer',
            'synopsis',
            'genre',
            'release_date',
            'price'
        )


class WriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writer
        fields = (
            'id',
            'name'
        )
