from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.db.models.functions import Lower
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from account.models import Account
from main.models import Admin

from django.shortcuts import render

def show_main(request):
    books = Book.objects.all()
    context = {
        'books' : books,
        'is_logged_in' : False,
        'user' : request.user,
        'admin' : 0,
        
    }
    if not request.user.is_authenticated:
        return render(request, "main.html", context)
    try:
        admin = (request.user.account.admin is not None)
    except Admin.DoesNotExist:
        return render(request, "main.html", context)

    
    context['admin'] = 1
    
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

