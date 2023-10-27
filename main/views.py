from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.db.models.functions import Lower
from django.http import JsonResponse

from django.shortcuts import render

def show_main(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    
    return render(request, "main.html", context)
    
def get_book_json(request, sort_mode):
    books = Book.objects.all().order_by(Lower(sort_mode))
    return HttpResponse(serializers.serialize('json', books))

def search_book_json(request, search_mode, sort_mode):
    if request.method == "POST":
        value = request.POST.get("search")
        if search_mode == "title":
            books = Book.objects.filter(title__icontains=value).order_by(Lower(sort_mode))
        else:
            books = Book.objects.filter(authors__icontains=value).order_by(Lower(sort_mode))
        return HttpResponse(serializers.serialize('json', books))

