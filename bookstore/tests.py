from django.test import TestCase
from .models import Book, Writer
class BookStoreTest(TestCase):

    def setUp(self):
        """ Setup a new writer and book """

        self.writer = Writer.objects.create(name='writertest')
        self.book = Book.objects.create(
            book_name = 'booktest',
            synopsis='this is a test',
            genre='fantasy',
            release_date='2022-09-01',
            price="15.15"
        )
        self.book.writer.set([self.writer.pk])
        self.book.save()

    def test_create_writer(self):
        """ Test create a new writer """

        writer = Writer.objects.get(name="writertest")

        self.assertEqual(writer, self.writer)

    def test_create_book_with_one_writer(self):
        """ Test create a new book with one writer """

        book = Book.objects.get(book_name="booktest")

        self.assertEqual(book, self.book)

    def test_create_book_with_two_writer(self):
        """ Test create a new book with two writer """

        self.secondWriter = Writer.objects.create(name='secondeWriterTest')
        self.book.writer.set([self.writer.pk, self.secondWriter.pk])
        book = Book.objects.get(book_name="booktest")

        created_book = list(self.book.writer.all())
        retrieved_book = list(book.writer.all())

        self.assertEqual(retrieved_book, created_book)
