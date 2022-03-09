import json

from django.test import TestCase, RequestFactory

from rest_framework.test import APIRequestFactory

from bookstore.models import Book, Writer
from .views import BookListView, WriterListView, BookSubListView, WriterSubListView,\
    SearchByGenres, CreateWriterView, CreateBookView, DeleteBookView, DeleteWriterView



class ApiTestView(TestCase):

    def setUp(self):
        """ Setup a new writer and book """

        self.factory = APIRequestFactory()
        self.writer_1 = Writer.objects.create(name='writertest_1')
        self.writer_2 = Writer.objects.create(name='writertest_2')

        self.book_1 = Book.objects.create(
            book_name = 'booktest_1',
            synopsis='This is the first test',
            genre='fantasy',
            release_date='2022-09-01',
            price="15.15"
        )
        self.book_2 = Book.objects.create(
            book_name = 'booktest_2',
            synopsis='This is the second test',
            genre='Classics',
            release_date='2001-11-01',
            price="25.27"
        )
        self.book_1.writer.set([self.writer_1.pk])
        self.book_1.save()
        self.book_2.writer.set([self.writer_2.pk])
        self.book_2.save()

    def test_book_list_view(self):
        """ Test list all books """

        request = self.factory.get('/books/', format='json')
        view = BookListView.as_view()
        response = view(request)

        book_1 = response.data['results'][0]['book_name']
        book_2 = response.data['results'][1]['book_name']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(book_1, 'booktest_1')
        self.assertEqual(book_2, 'booktest_2')

    def test_book_sub_list_view(self):
        """ Test Search on specific book """

        keyword = 'booktest_1'
        request = self.factory.get(f'/book/{keyword}', format='json')
        view = BookSubListView.as_view()
        response = view(request, item=keyword)
        book = response.data[0]['book_name']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(book, keyword)

    def test_writer_list_view(self):
        """ Test list all writers """

        request = self.factory.get('/writers/', format='json')
        view = WriterListView.as_view()
        response = view(request)
        writer_1 = response.data['results'][0]['name']
        writer_2 = response.data['results'][1]['name']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(writer_1, 'writertest_1')
        self.assertEqual(writer_2, 'writertest_2')

    def test_writer_sub_list_view(self):
        """ Test Search on specific writer """

        keyword = 'writertest_2'
        request = self.factory.get(f'/writer/{keyword}', format='json')
        view = WriterSubListView.as_view()
        response = view(request, item=keyword)
        writer = response.data[0]['name']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(writer, keyword)

    def test_search_by_genre(self):
        """ Test Search on genre """

        keyword = 'Classics'
        request = self.factory.get(f'/genre/{keyword}', format='json')
        view = SearchByGenres.as_view()
        response = view(request, item=keyword)
        genre = response.data[0]['genre']

        self.assertEqual(response.status_code , 200)
        self.assertEqual(genre, keyword)

    def test_creaet_writer(self):
        """ Test Create a Writer """

        payload = {
          "name": "Writer_1"
        }
        request = self.factory.post('/createwriter/', payload, format='json')
        view = CreateWriterView.as_view()
        response = view(request)

        self.assertEqual(response.status_code , 201)
        self.assertEqual(response.data['name'], 'Writer_1')

    def test_creaet_book(self):
        """ Test Create a Book """

        payload = {
          "book_name": "booktest_3",
          "writer": [self.writer_2.pk] ,
          "synopsis": "this is a test",
          "genre": "Classics",
          "release_date": "2022-03-08",
          "price": 10.00
        }
        request = self.factory.post('/createbook/', payload, format='json')
        view = CreateBookView.as_view()
        response = view(request)

        self.assertEqual(response.status_code , 201)
        self.assertEqual(response.data['book_name'], 'booktest_3')

    def test_delete_book(self):
        """ Test Delete a Book """

        request = self.factory.delete(f'/deletebook/{self.book_1.id}', format='json')
        view = DeleteBookView.as_view()
        response = view(request, id=self.book_1.id)

        self.assertEqual(response.status_code , 204)

    def test_delete_writer(self):
        """ Test Delete a Writer """

        request = self.factory.delete(f'/deletewriter/{self.writer_1.id}', format='json')
        view = DeleteWriterView.as_view()
        response = view(request, id=self.writer_1.id)

        self.assertEqual(response.status_code , 204)
