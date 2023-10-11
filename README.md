# Proyek Tengah Semester Kelompok A13

Ini tempat readme kita yaa

<h1>
  Anggota Kelompok
</h1>

- William Joel Matthew Quinn Rompis - 2206081843 </br>
- Adrial Natanael Liong - 2206026321 </br>
- Kezia Lasma Angelica - 2206082234 </br>
- Alifa Muhammad Hafidz - 2206082852 </br>
- Shafira Ramadhina Adifa  - 2206082972 </br>



<h1>
  Cerita Besar
</h1>
Berdasarkan tema utama yang diberikan, yaitu "Literasi dan Buku", kelompok kami mengembangkan ide proyek toko buku. Aplikasi toko buku yang kami buat terdiri atas 3 role user, yaitu Admin, Member, dan Non-Member dengan masing-masing <i>role</i> memiliki kapabilitas akses yang berbeda-beda. Pada halaman utama, aplikasi toko buku kami akan menampilkan data umum buku seperti judul, <i>cover</i>, dan harga dengan fitur <i>sort</i> berdasarkan peringkat tertentu juga fitur <i>filter</i> berdasarkan kategori tertentu. Selain itu, pada halaman utama juga terdapat <i>search bar</i> juga <i>navigation bar</i> yang dapat mengarahkan pengguna untuk <i>register</i> atau <i>login</i> atau menampilkan <i>username</i> dari <i>user</i> yang sedang <i>login</i> di aplikasi. Kemudian jika <i>user</i> melakukan klik pada buku yang diinginkan, user akan diarahkan ke halaman berisi info detail buku, dimana pada halaman tersebut juga tersedia <i>button</i> untuk <i>add cart</i> dan <i>checkout</i> (pada Member). Kami juga menyediakan halaman keranjang atau <i>cart</i>, dimana Member dapat melihat item buku yang sudah dimasukkan ke keranjangnya untuk <i>checkout</i>.  Pengiriman buku yang dipesan oleh Member dapat diatur oleh <i>role</i> Admin, dimana <i>role</i> Admin juga memiliki akses untuk melihat info seluruh Member dan dapat berganti ke mode user biasa jika diinginkan.



<h1>
  Penjelasan dan Pembagian Fitur
</h1>

Sumber database: https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv


<h2>
  Modul
</h2>

<h3>
  Main
</h3>

- PJ: William Joel Matthew Quinn Rompis 2206081843
- Berisi main page (member) dan main page (admin)
- Menampilkan semua buku yang tersedia di toko buku.
- Informasi buku yang ditampilkan: gambar buku, judul buku, pengarang buku, harga buku, dan rating buku
- Buku bisa diklik untuk mengalihkan ke book info page
- Ada search bar untuk search buku berdasarkan judul atau pengarang.
- Bisa sort/filter berdasarkan alphabetic, best-seller, top-rated.
- [Khusus admin] Ada opsi untuk menambah judul buku -- menambahkan buku baru ke dalam katalog, diarahkan ke book info page yang kosong

<h3>
  Book
</h3>

<h3>
  Order
</h3>

<h3>
  Payment
</h3>

<h3>
  Account
</h3>



<h2>
  Models list
</h2>


Models:
1. Account
   Username, Nama, email, password,

2. Buku
   Judul, pengarang, harga, kategori, deskripsi, jumlah halaman, stok, review, rating, jumlah terjual

3. Order
   Order id, Username, Buku, alamat, tanggal order, status(ongoing/completed), tanggal completed.

4. Review
   Reivew id, Username, Buku, rating, isi review, tanggal review.

5. Member
   Extends account, alamat, saldo, pesanan ongoing, buku yang telah dibeli, review

6. Admin
   Extends account, no. of books added, no. of orders completed.



<h2>
  Page List
</h2>


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
1. Non member:
   - Hanya dapat mengakses halaman main page (non member)
   - Dapat melihat informasi tentang buku, termasuk judul, pengarang, harga, dan rating
   - Jika ingin menambahkan buku ke keranjang (cart), user akan diminta untuk login atau melakukan pendaftaran
2. Member:
   - Dapat mengakses halaman "Main page (member)" dan fitur-fitur seluruh situs web
   - Bisa melihat dan membeli buku
   - Dapat menambahkan buku ke keranjang (cart) dan melakukan transaksi pembayaran
   - Memiliki saldo yang dapat diisi melalui halaman "Isi Saldo"
   - Dapat melihat semua pesanan yang pernah dibuat (baik yang masih berlangsung maupun yang sudah selesai) pada halaman "Order list (member)"
   - Dapat melihat informasi tentang akun mereka pada halaman "Account Info"
3. Admin:
   - Memiliki semua hak akses yang dimiliki oleh Member
   - Dapat mengakses halaman "Main page (admin)" yang memiliki semua fitur yang dimiliki oleh "Main page (member)."
   - Dapat menambahkan judul buku ke dalam katalog melalui halaman "Main page (admin)" dengan mengarahkan ke "Book info page (admin)."
   - Dapat mengedit informasi buku, termasuk menghapus buku dari katalog, Menambahkan buku, serta dapat mengedit deskripsi buku melalui "Book info page (admin)."
   - Dapat mengelola pesanan pada halaman "Order list (admin)" dan mengubah status pesanan menjadi "completed" melalui "Order page (admin)."
   - Dapat mengakses halaman "All Member Info" untuk melihat informasi seluruh anggota dan mengakses halaman "Member Info Page (admin)" untuk melihat detail tentang anggota tertentu.
   - Admin memiliki opsi untuk beralih ke mode "Member" untuk membeli buku seperti pengguna biasa.



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
