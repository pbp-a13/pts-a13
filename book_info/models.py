from django.db import models
from book.models import Book
# from account.models import Account, Review
from account.models import Account, Review

# Create your models here.
class Cart(models.Model):
    # member = models.ForeignKey(Account, on_delete=models.CASCADE)
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    jumlah_pembelian = models.IntegerField()