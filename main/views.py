from django.shortcuts import get_object_or_404, render
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.db.models.functions import Lower
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from account.models import Account, Review
from main.models import Admin

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
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



def show_admin_json(request):
    data = Admin.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def switch_mode_flutter(request):
    username_flutter = request.POST.get('username')
    user = User.objects.get(username=username_flutter)
    is_admin_mode = user.account.admin.is_admin_mode = not user.account.admin.is_admin_mode 
    user.account.admin.save()

    return JsonResponse({
        'is_admin_mode' : is_admin_mode
    })

@csrf_exempt
def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def get_review_json(request, id):
    try:
        book = Book.objects.get(pk=id)
        reviews = Review.objects.filter(book=book)
        return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")
    except Book.DoesNotExist:
        return HttpResponse("Book not found.", status=404)
    except Review.DoesNotExist:
        return HttpResponse("No reviews found for the specified book ID.", status=404)

@csrf_exempt
def delete_book_flutter(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk = id)
        book.delete()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def is_admin_mode(request):
    admin = Admin.objects.get(account=request.user)
    return HttpResponse(serializers.serialize('json', admin), content_type="application/json")

@csrf_exempt
def sort_review_flutter(request, sort_mode): 
    reviews = Review.objects.all().order_by(Lower(sort_mode))
    return HttpResponse(serializers.serialize('json', reviews))