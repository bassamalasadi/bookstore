import json
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from bookstore.models import Book, Writer
from .serializer import BookSerializer, WriterSerializer
from .pagination import SmallPagination


class CreateWriterView(generics.CreateAPIView):
    """ Create a new writer """

    serializer_class = WriterSerializer

    def post(self, request):
        name = self.request.data['name']
        if name:
            return self.create(request)

class CreateBookView(generics.CreateAPIView):
    """ Create a new book """

    serializer_class = BookSerializer

    def post(self, request):
        return self.create(request)

class BookListView(generics.ListAPIView):
    """ Get all books

        Return:
            List of books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = SmallPagination


class DeleteBookView(generics.DestroyAPIView):
    """ Delete a book """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def delete(self, request, id):
        return self.destroy(request, id)
    
class DeleteWriterView(generics.DestroyAPIView):
    """ Delete a writer """

    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'id'

    def delete(self, request, id):
        return self.destroy(request, id)


class BookSubListView(generics.ListAPIView):
    """ Search for a specific book
        Args:
            item : A specific keyword to search on books
        Return:
            List of books
    """
    serializer_class = BookSerializer

    def get_queryset(self, queryset=None, **kwargs):
        item = self.kwargs.get('item')
        try:
            response =  Book.objects.filter(book_name__contains=item)
            return response
        except Book.DoesNotExist:
            pass

class WriterListView(generics.ListAPIView):
    """ Get all writers

        Return:
            List of writers
    """
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    pagination_class = SmallPagination


class WriterSubListView(generics.ListAPIView):
    """ Search for a specific writer
        Args:
            item : A specific keyword to search on writers

        Return:
            List of writers
    """
    serializer_class = WriterSerializer

    def get_queryset(self, queryset=None, **kwargs):
        item = self.kwargs.get('item')
        try:
            response = Writer.objects.filter(name__contains=item)
            return response
        except Writer.DoesNotExist:
            pass


class SearchByGenres(generics.ListAPIView):
    """ Search on a list of genres
        Args:
            item : A specific keyword to search on genres

        Return:
            List of books for a specific genre
    """
    serializer_class = BookSerializer

    def get_queryset(self, queryset=None, **kwargs):
        item = self.kwargs.get('item')
        try:
            response = Book.objects.filter(genre__contains=item)
            return response
        except Writer.DoesNotExist:
            pass
