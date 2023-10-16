from django.shortcuts import render
from book.models import Book
from django.urls import path

from django.shortcuts import render

def show_main(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    
    return render(request, "main.html", context)
    
