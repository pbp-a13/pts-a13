from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    total_amount = models.PositiveIntegerField(default=0)