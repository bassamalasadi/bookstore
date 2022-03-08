from django.contrib import admin
from .models import Writer, Book

admin.site.register([Book, Writer])
