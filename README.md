# Proyek Tengah Semester Kelompok A13

Ini tempat readme kita yaa

<h1>
  Brainstorm
</h1>
<p> 
  Bagian ini berisi kumpulan ide-ide buat proyek kita. Kalau sudah fix akan dihapus.
</p>

<p>
  Joel: kalo gw biar ga rumit buat kyk toko buku aja.. jd bisa beli2 buku. Tapi stok buku dan saldo akun kita bisa langsung tambah manual. Kalo yg lain gmn?
</p>

<h1>
  Cerita Besar
</h1>

<h1>
  Toko buku
</h1>

<h1>
  Penjelasan dan Pembagian Fitur
</h1>

List fitur:
1. main_user - menampilkan buku yang tersedia (default: sort by abjad, opsi: sort by category), bisa menambah ke cart dari sini.
2. main_admin - menampilkan buku yang tersedia, bisa edit data (ubah deskripsi), tambah/kurang stok, tambah/hapus judul.
3. User Account system
4. order - proses pembelian termasuk cart, simulasi pengiriman, dst.
5. review dan rating - setiap buku bisa direview: berpengaruh pada rating buku
7. 

Landing page
Data user
Data buku


1. Main_user
halaman 1: menampilkan list buku yang tersedia, baik itu berdasarkan ranking, kategori, alfabet, dst
halaman 2: halaman per item: menampilkan nama, foto, harga, deskripsi, review, dst
halaman 3: 


2. Order
i) Add to cart

ii) Checkout

iii) Payment

iv) Menunggu pengiriman

v) review & rating




Models:

1. User
   Nama, email, password, saldo, buku yang dipesan, buku yang telah dibeli, review

2. Buku
   Judul, pengarang, harga, kategori, deskripsi, jumlah halaman, stok, review, rating





Landing Page:
List buku-buku yang ada. Pakai card (?). Setiap card menampilkan gambar buku, judul buku, dan harga buku. Bisa filter & sort buku berdasarkan harga, buku, rating. Bisa search buku.









Landing Page
1) Buku: judul, gambar, harga
3) Bisa filter buku & sort, search


Data User
1) User page
2) Bisa ngisi data diri ekstra
3) Saldo
4) Page tambah saldo
5) Buku yg sedang dipesan search

Data Buku
1) Judul, pengarang, dst, harga, kategori, deskripsi, jumlah halaman, stok
2) review, rating

ALgo beli buku:
- Tambah ke keranjang
- Halaman checkout
- Checkout
- Review page.

Admin:
- bisa switch mode admin mode user:
Mode admin:
- edit data buku (tambah judul, hapus judul, tambah stok, ganti yg lain2)
- Page daftar pesanan (simulasi pengiriman) -- instan kirim
