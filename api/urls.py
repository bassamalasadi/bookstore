from django.urls import path

from .views import BookListView, WriterListView, BookSubListView, WriterSubListView, \
    SearchByGenres, CreateWriterView, CreateBookView, DeleteBookView, DeleteWriterView

urlpatterns = [
    path('books/', BookListView.as_view(), name='Book'),
    path('book/<item>/', BookSubListView.as_view(), name='BookSubList'),
    path('writers/', WriterListView.as_view(), name='Writer'),
    path('writer/<item>/', WriterSubListView.as_view(), name='BookSubList'),
    path('Genre/<item>/', SearchByGenres.as_view(), name='SearchByGenres'),
    path('createwriter/', CreateWriterView.as_view(), name='CreateWriterView'),
    path('createbook/', CreateBookView.as_view(), name='CreateBookView'),
    path('deletebook/<int:id>/', DeleteBookView.as_view(), name='DeleteBookView'),
    path('deletewriter/<int:id>/', DeleteWriterView.as_view(), name='DeleteWriterView'),
]
