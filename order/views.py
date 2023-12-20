import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core import serializers



# Create your views here.
def member_orderlist_view(request):
    today = datetime.today()  # Dapatkan tanggal dan waktu saat ini

    # Membuat objek Order baru dengan order_date pada hari ini
    order = Order.objects.create(
        user=request.user,  # Ganti dengan user yang sesuai
        book=Book.objects.get(pk=1),  # Ganti dengan buku yang sesuai
        quantity=4,  # Ganti dengan jumlah yang sesuai
        order_date=today,
        estimated_delivery_date=datetime(2023, 10, 30, 12, 0, 0),
    )

    context = {
        'title': 'Laut Bercerita',
        'quantity': order.quantity,
        'order_date': order.order_date,
        'price': 109000,
        'estimated_delivery_date' : order.estimated_delivery_date
    }
    return render(request, 'member_orderlist.html', context)



@csrf_exempt
# views.py
def apply_sort(request):
    if request.is_ajax() and request.method == "POST":
        filter_value = request.POST.get('filter_value')
        # Lakukan sort berdasarkan nilai filter (misalnya, berdasarkan total harga)
        # ...
        # Kirim data yang telah diurutkan sebagai respons
        sorted_data = {...}
        return JsonResponse(sorted_data)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


def all_books(request):
    books = Book.objects.all()
    # for order in Order.objects.all():
    #     order.delete()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_all_orders(request):
    orders = Order.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', orders), content_type="application/json")

@csrf_exempt
def get_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.filter(pk=data["pk"])
        return HttpResponse(serializers.serialize('json', book), content_type="application/json")

    return HttpResponse(serializers.serialize('json', []), content_type="application/json")

@csrf_exempt
def show_user_orders(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filter = data["filter"]
        if filter == "completed":
            orders = orders = Order.objects.filter(user=request.user, is_completed=True)
        else:
            orders = orders = Order.objects.filter(user=request.user, is_completed=False)
        return HttpResponse(serializers.serialize('json', orders), content_type="application/json")
    
    return HttpResponse(serializers.serialize('json', []), content_type="application/json")

@csrf_exempt
def make_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=data["pk"])
        order, created = Order.objects.get_or_create(
            user=request.user, 
            book=book, 
            is_completed=False,
            defaults={'quantity': 1}
        )
        if created:
            return JsonResponse({"status": True}, status=200)
        return JsonResponse({"status": False}, status=200)
    
    return JsonResponse({"status": False}, status=400)

@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.get(pk=data["order_id"])
        order.quantity += 1
        order.save()
        return JsonResponse({"status": True}, status=200)
    
    return JsonResponse({"status": False}, status=400)

@csrf_exempt
def minus_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.get(pk=data["order_id"])
        order.quantity -= 1
        order.save()
        if order.quantity == 0:
            order.delete()
        return JsonResponse({"status": True}, status=200)
    
    return JsonResponse({"status": False}, status=400)

@csrf_exempt
def complete_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.get(pk=data["order_id"])
        if order.is_completed == False:
            order.is_completed = True
            order.save()
            return JsonResponse({"status": True}, status=200)
    
    return JsonResponse({"status": False}, status=400)
    