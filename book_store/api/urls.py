from django.urls import path
from book_store.api.views import BooksDetails, BookList
urlpatterns = [

    path('books/', BookList.as_view(), name='books-list'),
    path('books/<int:pk>', BooksDetails.as_view(), name='book-detail'),

]

