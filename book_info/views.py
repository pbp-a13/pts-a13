from pyexpat.errors import messages
from django import template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from book.models import Book
from account.models import Account, Review
from book_info.forms import BookForm
from book_info.models import Cart
from main.models import Admin
from cart.models import CartItem
from django.contrib.auth.models import User

# Create your views here.
def is_admin(user):
    return user.is_authenticated and user.is_staff

def show_info(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book=book)

    if request.user.is_authenticated:
        user = request.user
    else:
        user, created = User.objects.get_or_create(username='anonymous')

    cart, created = Cart.objects.get_or_create(user=user, book=book)
    context = {
        'book': book,
        'reviews': reviews,
        'cart': cart,
    }

    if cart.total_amount == 0:
        cart.delete()

    return render(request, "book_info.html", context)

def edit_book(request, id):
    # Get book berdasarkan ID
    book = Book.objects.get(pk = id)

    # Set book sebagai instance dari form
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman book-info
        form.save()
        return HttpResponseRedirect(reverse('book_info:show_info', args=[str(book.pk)]))

    context = {'form': form}
    return render(request, "edit_book.html", context)

def delete_book(request, id):
    # Get data berdasarkan ID
    book = Book.objects.get(pk = id)
    # Hapus data
    book.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('book_info:show_info', args=[str(book.pk)]))

def add_to_cart(request, id, amount):
    book = get_object_or_404(Book, pk=id)
    # cartItem, created = CartItem.objects.get_or_create(user=request.user, books=book)
    cart_entry, created = Cart.objects.get_or_create(user=request.user, book=book, amount=amount)

    if (cart_entry.total_amount + cart_entry.amount) <= book.stock:
        cart_entry.total_amount += cart_entry.amount
    cart_entry.amount = 1
    cart_entry.save()
    return HttpResponseRedirect(reverse('book_info:show_info', args=[str(book.pk)]))

def get_cart_json(request):
    carts = Cart.objects.filter(user=request.user)
    cart_list = []
    for cart in carts:
        if cart.total_amount > 0:
            cart_dict = {
                'ID Item': cart.pk,
                'Book': {
                    'pk': cart.book.pk,
                    'Total amount': cart.total_amount,
                    },
            }
            cart_list.append(cart_dict)
    return JsonResponse(cart_list, safe=False)
    # return HttpResponse(serializers.serialize('json', carts), content_type="application/json")

def increment_amount(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.user.is_authenticated:
        user = request.user
    else:
        user, created = User.objects.get_or_create(username='anonymous')

    cart_entry, created = Cart.objects.get_or_create(user=user, book=book)
    if cart_entry.amount < book.stock:
        cart_entry.amount += 1
        cart_entry.save()

    return HttpResponseRedirect(reverse('book_info:show_info', args=[str(book.pk)]))

def decrement_amount(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.user.is_authenticated:
        user = request.user
    else:
        user, created = User.objects.get_or_create(username='anonymous')
        
    cart_entry, created = Cart.objects.get_or_create(user=user, book=book)
    if cart_entry.amount > 1:
        cart_entry.amount -= 1
        cart_entry.save()

    return HttpResponseRedirect(reverse('book_info:show_info', args=[str(book.pk)]))

def get_review_json(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', reviews))

def search_review_json(request, search_mode):
    if request.method == "POST":
        if search_mode == "semua":
            reviews = Review.objects.all()
        elif search_mode == "5":
            reviews = Review.objects.filter(rating=5)
        elif search_mode == "4":
            reviews = Review.objects.filter(rating=4)
        elif search_mode == "3":
            reviews = Review.objects.filter(rating=3)
        elif search_mode == "2":
            reviews = Review.objects.filter(rating=2)
        elif search_mode == "1":
            reviews = Review.objects.filter(rating=1)
        return HttpResponse(serializers.serialize('json', reviews))

@csrf_exempt
def edit_book_flutter(request, book_id):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Menggunakan get_object_or_404 untuk mendapatkan objek atau memberikan respons 404 jika tidak ditemukan
        book = get_object_or_404(Book, id=book_id)

        # Melakukan pembaruan pada atribut objek yang ada
        book.fields.authors = data.get("authors", book.fields.authors)
        book.fields.title = data.get("title", book.fields.title)
        book.fields.price = int(data.get("price", book.fields.price))
        book.fields.stock = int(data.get("stock", book.fields.stock))

        # Menyimpan perubahan ke dalam database
        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

# @csrf_exempt
# def filter_review_flutter(request, sort_mode): 
#     # data = json.loads(request.body)
#     # user = request.user,
#     if sort_mode == "Low to High":
#         reviews = Review.objects.order_by(Lower(data["rating"]))
#     else:
#         reviews = Review.objects.order_by(Lower(data["rating"))

#     return HttpResponse(serializers.serialize('json', reviews))