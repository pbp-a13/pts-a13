from django.forms import ModelForm
from book.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'authors', 'categories', 'stock']
        