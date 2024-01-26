from django.urls import path
from myBookStore.api.views import BookInfo, GetBooks
urlpatterns = [

    path('books/', BookInfo.as_view(), name='list-of-books'),
    path('books/<int:pk>', GetBooks.as_view(), name='Info-of-books'),
    

]

