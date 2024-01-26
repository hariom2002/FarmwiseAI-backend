from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import BookStore

class BookStoreModelTest(TestCase):
    def setUp(self):
        self.book = BookStore.objects.create(
            title="Test Book",
            author="Test Author",
            ISBN="17334444567890",
            price=20,
            quantity=10
        )

    def test_bookstore_model(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.ISBN, "17334444567890")
        self.assertEqual(self.book.price, 20)
        self.assertEqual(self.book.quantity, 10)

class BookStoreAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "ISBN": "17334567890",
            "price": 20,
            "quantity": 10
        }
        self.book = BookStore.objects.create(**self.book_data)
        self.url = reverse("books-list")

    def test_get_book_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # def test_create_book(self):
    #     response = self.client.post(self.url, self.book_data, format='json')
    #     print(response.data)  # Add this line to print the response data
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(BookStore.objects.count(), 2)


    def test_get_book_details(self):
        url = reverse("book-detail", args=[self.book.ISBN])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book.ISBN])
        updated_data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "ISBN": "17334444567890",
            "price": 25,
            "quantity": 15
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price'], 25)

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book.ISBN])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookStore.objects.count(), 0)
