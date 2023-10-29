from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound



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



