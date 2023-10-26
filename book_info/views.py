from django.shortcuts import render

# Create your views here.
def show_info(request):
    context = {
        'authors': 'Leila S. Chudori',
        'title': 'Laut Bercerita',
        'categories': 'Fantasi',
        'price': 109000,
        'description': 'Buku ini terdiri atas dua bagian. Bagian pertama mengambil sudut pandang seorang mahasiswa aktivis bernama Laut, menceritakan bagaimana Laut dan kawan-kawannya menyusun rencana, berpindah-pindah dalam pelarian, hingga tertangkap oleh pasukan rahasia. Sedangkan bagian kedua dikisahkan oleh Asmara, adik Laut. Bagian kedua mewakili perasaan keluarga korban penghilangan paksa, bagaimana pencarian mereka terhadap kerabat mereka yang tak pernah kembali.',
        'stock': 1550,
        'jumlah_terjual': 44,
    }

    return render(request, "book_info.html", context)

