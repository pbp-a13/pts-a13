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
from django.views.decorators.csrf import csrf_exempt

import json

def show_main(request):
    books = Book.objects.all()
    context = {
        'books' : books,
        'is_logged_in' : False,
        'user' : request.user,
        'admin' : 0,
        'is_admin_mode': 0
        
    }
    if not request.user.is_authenticated:
        return render(request, "main.html", context)
    try:
        admin = (request.user.account.admin is not None)
    except Admin.DoesNotExist:
        return render(request, "main.html", context)
    except Account.DoesNotExist:
        return render(request, "main.html", context)

    
    context['admin'] = 1
    if request.user.account.admin.is_admin_mode:
        context['is_admin_mode'] = 1
    else:
        context['is_admin_mode'] = 0
    
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
    
def switch_mode(request):
    request.user.account.admin.is_admin_mode = not request.user.account.admin.is_admin_mode
    request.user.account.admin.save()
    return show_main(request)


def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# @csrf_exempt
# def search_book_flutter(request):
#     if request.method == 'POST':
        
#         data = json.loads(request.body)
#         user = request.user,
#         value = data["value"],
#         search_mode = data["search_mode"],
#         sort_mode = data["sort_mode"]
#         if search_mode == "title":
#             books = Book.objects.filter(title__icontains=value).order_by(Lower(sort_mode))
#         else:
#             books = Book.objects.filter(authors__icontains=value).order_by(Lower(sort_mode))

#         return HttpResponse(serializers.serialize('json', books))
    
@csrf_exempt
def search_book_flutter(request, value, search_mode, sort_mode): 
    # data = json.loads(request.body)
    # user = request.user,
    # value = data["value"],
    # search_mode = data["search_mode"],
    # sort_mode = data["sort_mode"]
    if value == "*None*":
        value = ""
    if search_mode == "title":
        books = Book.objects.filter(title__icontains=value).order_by(Lower(sort_mode))
    else:
        books = Book.objects.filter(authors__icontains=value).order_by(Lower(sort_mode))

    return HttpResponse(serializers.serialize('json', books))
