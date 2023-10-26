from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from account.models import Account, Review
from book_info.models import Cart

# Create your views here.
def show_info(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member = request.user
    cart_entry, created = Cart.objects.get_or_create(member=member, book=book)
    context = {
        'authors': 'Leila S. Chudori',
        'title': 'Laut Bercerita',
        'categories': 'Fantasi',
        'price': 109000,
        'description': 'Buku ini terdiri atas dua bagian. Bagian pertama mengambil sudut pandang seorang mahasiswa aktivis bernama Laut, menceritakan bagaimana Laut dan kawan-kawannya menyusun rencana, berpindah-pindah dalam pelarian, hingga tertangkap oleh pasukan rahasia. Sedangkan bagian kedua dikisahkan oleh Asmara, adik Laut. Bagian kedua mewakili perasaan keluarga korban penghilangan paksa, bagaimana pencarian mereka terhadap kerabat mereka yang tak pernah kembali.',
        'stock': 1550,
        'jumlah_terjual': 44,
        'jumlah_pembelian': 1,
        'initial_quantity': cart_entry.jumlah_pembelian,
    }

    return render(request, "book_info.html", context)

@csrf_exempt
def increment_amount(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member = request.user 

    cart_entry, created = Cart.objects.get_or_create(member=member, book=book)
    cart_entry.jumlah_pembelian += 1
    cart_entry.save()

    return JsonResponse({'success': True})

@csrf_exempt
def decrement_amount(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member = request.user  # Assuming you have a logged-in user

    cart_entry, created = Cart.objects.get_or_create(member=member, book=book)
    if cart_entry.jumlah_pembelian > 0:
        cart_entry.jumlah_pembelian -= 1
        cart_entry.save()

    return JsonResponse({'success': True})