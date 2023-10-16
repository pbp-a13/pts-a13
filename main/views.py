from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render

def show_main(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    
    return render(request, "main.html", context)
    
def get_book_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))
