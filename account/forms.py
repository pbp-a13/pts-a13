from django.forms import ModelForm
from account.models import Account
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']



class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['alamat', 'nama', 'email',]