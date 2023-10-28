from django.contrib import admin
from .models import Account
from main.models import Admin

admin.site.register(Account)
admin.site.register(Admin)
