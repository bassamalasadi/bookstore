from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name =  models.CharField(max_length = 200, unique=True)
    writer = models.ManyToManyField(Writer)
    synopsis = models.TextField()
    genre = models.CharField(max_length = 200)
    release_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.book_name
