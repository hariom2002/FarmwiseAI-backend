from book_store.models import BookStore
from rest_framework import serializers
class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStore
        fields = "__all__"