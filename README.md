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

Sumber database: [insert here]



List Page:
1. Main page (admin dan member)
2. Account info page (per account)
3. Book info page (admin & member)
4. Cart page
5. Order list page - list of ongoing and completed orders (admin & member)
6. Order page - detail dari masing-masing order (admin & member)
7. Isi saldo page
8. Payment page
9. All users info (Admin only)
10. Member Info Page (Admin only)



Models:
1. Account
   IsAdmin, Username, Nama, email, password, saldo, pesanan ongoing, buku yang telah dibeli, review

2. Buku
   Judul, pengarang, harga, kategori, deskripsi, jumlah halaman, stok, review, rating, jumlah terjual

3. Order
   Order id, Username, Buku, tanggal order, status(ongoing/completed), tanggal completed.

4. Review
   Reivew id, Username, Buku, rating, isi review, tanggal review.

<h3>
  Main page (member)
</h3>

- Menampilkan buku-buku yang tersedia pada toko buku.
- Informasi buku yang ditampilkan: gambar buku, judul buku, pengarang buku, harga buku, dan rating buku
- Buku bisa diklik untuk mengalihkan ke book info page
- Ada search bar untuk search buku berdasarkan judul atau pengarang.
- Bisa sort/filter berdasarkan alphabetic, best-seller, top-rated.

<h3>
  Main page (admin)
</h3>

- memiliki semua fitur yang dimiliki main mage (member).
- Ada opsi untuk menambah judul buku -- menambahkan buku baru ke dalam katalog, diarahkan ke book info page yang kosong

<h3>
  Book info page (member)
</h3>

- Menampilkan semua informasi tentang buku
- Jika stok tersedia, bisa menambahkan dan mengurangi item ke/dari cart.

<h3>
  Book info page (non-member)
</h3>

- Menampilkan semua informasi tentang buku
- Jika ingin menambahkan item ke cart, akan diminta untuk login/signup

<h3>
  Book info page (admin)
</h3>

- Menampilkan semua informasi tentang buku.
- Ada opsi delete judul -- menghapus buku dari katalog
- Ada tombol "edit" yang akan mengubah semua tampilan menjadi form sehingga bisa dimodifikasi. Setelah itu ada tombol "Save" untuk menyimpan modifikasi.
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

- Menampilkan total harga yang harus dibayar, dan saldo member yang tersedia
- Ada tombol untuk mengarahkan ke page isi saldo
- Tombol bayar: memasukkan buku ke order list, dan mengurangi saldo member dengan harga total buku.
- Tombol bayar tidak bisa diklik jika saldo kurang dari harga yang harus dibayar


<h3>
  Order list page (admin)
</h3>

- Berisi semua order yang pernah dilakukan, oleh semua member, baik ongoing ataupun completed (ada dua section)
- Setiap order memiliki informasi username, judul buku yang dibeli, serta jumlahnya.
- Setiap order dapat diklik untuk mengarahkan ke order page (admin)

<h3>
  Order page (admin)
</h3>

- Berisi semua detail tentang satu order spesifik.
- Untuk ongoing order, ada tombol "Kirim" --> mengubah status order menjadi completed. 


<h3>
  Order list page (member)
</h3>

- Berisi semua order yang pernah dilakukan oleh member, baik ongoing ataupun completed (ada dua section)
- Setiap order memiliki informasi username, judul buku yang dibeli, serta jumlahnya.
- Setiap order dapat diklik untuk mengarahkan ke order page (member)

<h3>
  Order page (member)
</h3>

- Berisi semua detail tentang satu order spesifik. (jenis dan jumlah buku yang dipesan, kapan dipesan, kapan diperkirakan akan sampai pesanannya)

<h3>
  Isi Saldo Page
</h3>

- Member dapat meng-input jumlah top-up saldo lalu menekan tombol "Isi" untuk mengupdate saldo.


<h3>
  Account Info Page
</h3>

- User dapat melihat semua informasi tentang account.
- Ada tombol "edit" yang akan mengubah semua tampilan menjadi form sehingga bisa dimodifikasi. Setelah itu ada tombol "Save" untuk menyimpan modifikasi.

<h3>
  All Member Info (admin only) 
</h3>

- List semua member yang ada, menampilkan username, tanggal join, dan jumlah order yang pernah dibuat
- Setiap member bisa diklik untuk melihat member info page masing-masing.

<h3>
  Member Info Page (admin only) 
</h3>

- dapat melihat informasi umum sebuah member seperti nama, username, saldo, pesanan ongoing, buku yang telah dibeli, review

<h3>
  Register Page
</h3>
- halaman untuk register menjadi member
- Isinya mirip account info page tapi form kosong, beserta input username & password

<h3>
  General
</h3>

- Terdapat navbar pada setiap halaman untuk dapat berpindah-pindah ke semua halaman yang tidak buku-spesifik atau order-spesifik
- Admin memiliki opsi untuk berganti ke member-mode jika ingin membeli buku seperti member.
- Ada tiga  jenis user:
1. Non member: Hanya bisa melihat-lihat buku, tidak bisa membeli
2. Member: bisa membeli buku
3. Admin: Bisa mengedit buku, mengirim order, dan bisa switch ke mode member untuk membeli buku.



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
halaman 1: halaman utama: menampilkan list buku yang tersedia, baik itu berdasarkan ranking, kategori, alfabet, dst
halaman 2: halaman per item: menampilkan nama, foto, harga, deskripsi, review, dst

<h4>kykny gaperlu deh</h4> 

halaman 3: halaman user: mengubah/menambah informasi user
halaman 4: halaman isi saldo: bisa mengisi jumlah saldo yang diingin dengan masukan jumlah uang yang ingin dimasukan dan uang tersebut akan tambah dengan saldo sekarang
halaman 5: halaman list order: menampilkan setiap order yang pernah dilakukan user
halaman 6: halaman order: menampilkan sebuah order yang telah dipilih pada halaman list order (halaman 6) dan menampilkan jenis dan jumlah setiap buku yang dipesan pada sebuah order, kapan pesanan dilakukan, dan status pesanan, dan tanggal selesai(kalau sudah selesai)
halaman 7: halaman keranjang: menampilkan setiap buku yang sudah dipesan dan jumlah setiap buku yang sudah dipesan, jumlah harga, dan tombol bayar untuk mengkonfirmasi pemesanan buku
halaman 8: halaman review: menampilkan setiap buku yabng pernah dipesan dan bisa click setiap buku untuk member review

3. Main_admin
halaman 1: halaman utama: menampilkan list buku yang tersedia, dan bisa mengubah data buku tersebut
halaman 2: halaman per item: menampilkan nama, foto, harga, deskripsi, review dan bisa diubah


4. Order
i) Add to cart

ii) Checkout

iii) Payment

iv) Menunggu pengiriman

v) review & rating

Landing Page:
List buku-buku yang ada. Pakai card (?). Setiap card menampilkan judul buku, stock buku yang ada, pilihan untuk masukan ke keranjang, tahun publikasi, penulis buku. Bisa filter & sort buku berdasarkan harga, buku, rating. Bisa search buku.

Landing Page
1) Buku: judul, gambar, harga
2) Bisa filter buku, sort buku, search buku spesifik


Data User
1) User page
2) Bisa ngisi data diri ekstra
3) Saldo
4) Page tambah saldo
5) Buku yg sedang dipesan search

Data Buku
1) Judul, pengarang, harga, kategori, deskripsi, jumlah halaman, stok
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
