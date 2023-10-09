# Proyek Tengah Semester Kelompok A13

Ini tempat readme kita yaa

<h1>
  Brainstorm
</h1>


<h1>
  Cerita Besar
</h1>

<h1>
  Toko buku
</h1>

<h1>
  Penjelasan dan Pembagian Fitur
</h1>


List Page:
1. Main page (admin dan user)
2. User info page (per user)
3. Book info page (admin & user)
4. Cart page
5. Order page - list of ongoing and completed orders (admin & user)
6. Isi saldo page
7. Payment page
8. All users info (Admin only)
9. Ongoi


Models:
1. User
   Nama, email, password, saldo, pesanan ongoing, buku yang telah dibeli, review

2. Buku
   Judul, pengarang, harga, kategori, deskripsi, jumlah halaman, stok, review, rating, jumlah terjual

<h3>
  Main page (user)
</h3>

- Menampilkan buku-buku yang tersedia pada toko buku.
- Informasi buku yang ditampilkan: gambar buku, judul buku, pengarang buku, harga buku, dan rating buku
- Buku bisa diklik untuk mengalihkan ke book info page
- Ada search bar untuk search buku berdasarkan judul atau pengarang.
- Bisa sort/filter berdasarkan alphabetic, best-seller, top-rated.

<h3>
  Main page (admin)
</h3>
- memiliki semua fitur yang dimiliki main mage (user).
- Ada opsi untuk menambah judul buku -- menambahkan buku baru ke dalam katalog, diarahkan ke book info page yang kosong

<h3>
  Book info page (user)
</h3>
- Menampilkan semua informasi tentang buku
- Jika stok tersedia, bisa menambahkan dan mengurangi item ke/dari cart.

<h3>
  Book info page (admin)
</h3>
- Menampilkan semua informasi tentang buku, namun bisa diedit (berbentuk form).
- Ada opsi delete judul -- menghapus buku dari katalog
- Jika sedang menambah judul buku, akan menampilkan form kosong


<h3>
  Cart page
</h3>
- Berisi daftar buku-buku yang ada di cart, harganya, dan total harga
- Bisa tambah dan kurang jumlah untuk masing-masing item
- Bisa remove item dari cart
- Ada tombol menuju payment page

<h3>
  Payment page
</h3>
- Menampilkan total harga yang harus dibayar, dan saldo user yang tersedia
- Ada tombol untuk mengarahkan ke page isi saldo
- Tombol bayar: memasukkan buku ke order list, dan mengurangi saldo user dengan harga total buku.
- Tombol bayar tidak bisa diklik jika saldo kurang dari harga yang harus dibayar


<h3>
  Order page (admin)
</h3>


<h1>
  Brainstorm
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










Landing Page:
List buku-buku yang ada. Pakai card (?). Setiap card menampilkan . Bisa filter & sort buku berdasarkan harga, buku, rating. Bisa search buku.









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
