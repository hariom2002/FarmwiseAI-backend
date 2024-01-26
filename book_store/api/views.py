from book_store.models import BookStore
from rest_framework import generics
from book_store.api.serializers import BookStoreSerializer
from rest_framework.permissions import IsAuthenticated
class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookStore.objects.all()
    serializer_class = BookStoreSerializer
    
class BooksDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookStore.objects.all()
    serializer_class = BookStoreSerializer