from django.db import models

# Create your models here.
# (e.g., title, author, 
# ISBN, price, quantity)
class BookStore(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50, primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title + " | " + self.author + " | " + str(self.price) + "|" + self.ISBN + " | " + str(self.price)
    