from django.db import models
from account.models import Account
from account.models import Account
from django.contrib.auth.models import User

class Admin(Account):
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    orders_completed = models.IntegerField(default=0)
    books_added = models.IntegerField(default=0)