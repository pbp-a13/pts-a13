from django import template
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from account.models import Account, Review
# from book_info.forms import BookForm
from book_info.models import Cart
from main.models import Admin

# Create your views here.
def show_info(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book=book)
    # carts = Cart.objects.filter(member=request.user)
    context = {
        # dummy
        # 'authors': 'Leila S. Chudori',
        # 'title': 'Laut Bercerita',
        # 'categories': 'Fantasi',
        # 'price': 109000,
        # 'description': 'Buku ini terdiri atas dua bagian. Bagian pertama mengambil sudut pandang seorang mahasiswa aktivis bernama Laut, menceritakan bagaimana Laut dan kawan-kawannya menyusun rencana, berpindah-pindah dalam pelarian, hingga tertangkap oleh pasukan rahasia. Sedangkan bagian kedua dikisahkan oleh Asmara, adik Laut. Bagian kedua mewakili perasaan keluarga korban penghilangan paksa, bagaimana pencarian mereka terhadap kerabat mereka yang tak pernah kembali.',
        # 'stock': 1550,
        # 'jumlah_terjual': 44,
        # 'jumlah_pembelian': 1,

        'book': book,
        'reviews': reviews,
        # 'carts': carts,
    }

    return render(request, "book_info.html", context)

register = template.Library()
@register.filter(name='is_admin')
def is_admin(user):
    return Admin.objects.filter(user=user).exists()

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
    return HttpResponseRedirect(reverse('book_info:show_info'))

@csrf_exempt
def increment_amount(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member = request.user 

    cart_entry, created = Cart.objects.get_or_create(member=member, book=book)
    if cart_entry.jumlah_pembelian < book.stock:
        cart_entry.jumlah_pembelian += 1
        cart_entry.save()

    return JsonResponse({'success': True})

@csrf_exempt
def decrement_amount(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member = request.user

    cart_entry, created = Cart.objects.get_or_create(member=member, book=book)
    if cart_entry.jumlah_pembelian > 0:
        cart_entry.jumlah_pembelian -= 1
        cart_entry.save()

    return JsonResponse({'success': True})