from django.forms import ModelForm
from account.models import Account

class Account(ModelForm):
    class Meta:
        model = Account
        fields = ['alamat', 'nama', 'email', 'buku_dibeli', 'saldo']