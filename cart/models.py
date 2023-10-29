from django.db import models
from django.contrib.auth.models import User
from book_info.models import Book

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        total = sum([book.price for book in self.books.all()])  # Menghitung total subtotal
        return total * self.quantity
