## Implementasi Hash Map pada Pencarian Data Tiket Bioskop Berdasarkan Kode Booking
**A. Judul Program :** Implementasi Hash Map pada Pencarian Data Tiket Bioskop Berdasarkan Kode Booking

**B. Deskripsi Singkat :** Program ini dibuat untuk menerapkan struktur data Hash Map pada sistem pencarian data tiket bioskop berdasarkan kode booking. Dalam program ini, kode booking digunakan sebagai key, sedangkan data tiket seperti nama pembeli, judul film, jam tayang, studio, dan nomor kursi digunakan sebagai value. Dengan menggunakan kode booking, data tiket dapat dicari dengan lebih cepat tanpa harus menelusuri seluruh data satu per satu.

Metode yang digunakan dalam program ini adalah Separate Chaining, yaitu cara menangani collision atau tabrakan data pada indeks hash yang sama. Jika terdapat beberapa kode booking yang menghasilkan indeks yang sama, maka data tersebut akan disimpan dalam bentuk linked list pada indeks tersebut. Program ini juga menyediakan fitur untuk menambahkan data tiket, mencari data tiket, menghapus data tiket, dan menampilkan seluruh isi hash table.

**C. Source Code :** 

<img width="1186" height="5622" alt="code-snapshot32" src="https://github.com/user-attachments/assets/ccf10a20-6c17-442a-825e-aaaf181bab0f" />

**BAGIAN 1. BAGIAN CLASS NODE:**

`class Node:` digunakan untuk membuat class bernama Node. Class ini berfungsi sebagai tempat untuk membuat satu data atau satu simpul pada Hash Map Separate Chaining.

`def __init__(self, key, value):` digunakan sebagai constructor, yaitu fungsi yang otomatis berjalan ketika objek Node dibuat. Parameter `key` digunakan untuk menyimpan kode booking, sedangkan `value` digunakan untuk menyimpan data tiket bioskop.

`self.key = key` digunakan untuk menyimpan nilai kode booking ke dalam variabel `key`. Jadi setiap node memiliki data utama berupa kode booking.

`self.value = value` digunakan untuk menyimpan isi data tiket bioskop ke dalam variabel `value`. Data ini berisi nama pembeli, judul film, jam tayang, studio, dan nomor kursi.

`self.next = None` digunakan untuk membuat penghubung ke node berikutnya. Nilai awalnya `None` karena saat node baru dibuat, node tersebut belum terhubung dengan node lain.

**BAGIAN 2. BAGIAN CLASS HASHMAPSEPARATECHAINING:**

`class HashMapSeparateChaining:` digunakan untuk membuat class utama bernama HashMapSeparateChaining. Class ini berfungsi untuk mengatur penyimpanan, pencarian, penghapusan, dan penampilan data tiket bioskop menggunakan Hash Map.

`def __init__(self, size=10):` digunakan sebagai constructor untuk membuat hash table dengan ukuran awal 10. Jika tidak diberikan ukuran lain, maka ukuran tabel otomatis bernilai 10.

`self.SIZE = size` digunakan untuk menyimpan ukuran hash table ke dalam variabel `SIZE`. Ukuran ini dipakai untuk menentukan jumlah indeks pada tabel.

`self.table = [None] * self.SIZE` digunakan untuk membuat tabel hash yang berisi nilai awal `None`. Artinya, semua indeks pada hash table masih kosong.

**BAGIAN 3. BAGIAN FUNGSI HASH:**

`def hash_function(self, key):` digunakan untuk membuat fungsi hash. Fungsi ini bertugas mengubah kode booking menjadi indeks pada hash table.

`return (key % self.SIZE + self.SIZE) % self.SIZE` digunakan untuk menentukan posisi indeks dari kode booking. Dengan rumus ini, kode booking akan dibagi berdasarkan ukuran tabel sehingga hasilnya tetap berada dalam batas indeks hash table.

**BAGIAN 4. BAGIAN FUNGSI INSERT:**

`def insert(self, key, value):` digunakan untuk menambahkan data tiket bioskop ke dalam hash table. Parameter `key` berisi kode booking, sedangkan `value` berisi data tiket bioskop.

`index = self.hash_function(key)` digunakan untuk mencari indeks tempat data tiket akan disimpan berdasarkan kode booking yang dimasukkan.

`current = self.table[index]` digunakan untuk mengambil data pertama yang berada pada indeks tersebut. Jika indeks masih kosong, maka nilainya adalah `None`.

`while current is not None:` digunakan untuk melakukan perulangan selama pada indeks tersebut masih terdapat node atau data.

`if current.key == key:` digunakan untuk mengecek apakah kode booking yang dimasukkan sudah ada di dalam hash table.

`current.value = value` digunakan untuk memperbarui data tiket apabila kode booking yang sama sudah ditemukan.

`return` digunakan untuk menghentikan proses insert setelah data tiket berhasil diperbarui.

`current = current.next` digunakan untuk berpindah ke node berikutnya jika kode booking belum ditemukan pada node saat ini.

`new_node = Node(key, value)` digunakan untuk membuat node baru yang berisi kode booking dan data tiket bioskop.

`new_node.next = self.table[index]` digunakan untuk menghubungkan node baru ke node lama yang sudah ada pada indeks tersebut. Bagian ini dipakai ketika terjadi collision.

`self.table[index] = new_node` digunakan untuk menyimpan node baru pada indeks hash table. Node baru akan diletakkan di bagian paling depan.

**BAGIAN 5. BAGIAN FUNGSI SEARCH:**

`def search(self, key):` digunakan untuk mencari data tiket bioskop berdasarkan kode booking yang dimasukkan.

`index = self.hash_function(key)` digunakan untuk menentukan indeks tempat data tiket kemungkinan disimpan.

`current = self.table[index]` digunakan untuk mengambil node pertama pada indeks tersebut.

`while current is not None:` digunakan untuk melakukan perulangan selama node pada indeks tersebut masih ada.

`if current.key == key:` digunakan untuk mengecek apakah kode booking pada node saat ini sama dengan kode booking yang dicari.

`return current` digunakan untuk mengembalikan node jika data tiket berhasil ditemukan.

`current = current.next` digunakan untuk berpindah ke node berikutnya jika kode booking belum sesuai.

`return None` digunakan jika data tiket dengan kode booking tersebut tidak ditemukan.

**BAGIAN 6. BAGIAN FUNGSI REMOVE_KEY:**

`def remove_key(self, key):` digunakan untuk menghapus data tiket bioskop berdasarkan kode booking.

`index = self.hash_function(key)` digunakan untuk menentukan indeks tempat data tiket yang ingin dihapus kemungkinan berada.

`current = self.table[index]` digunakan untuk mengambil node pertama pada indeks tersebut.

`prev = None` digunakan untuk menyimpan node sebelumnya. Nilai awalnya `None` karena pada awal pencarian belum ada node sebelumnya.

`while current is not None:` digunakan untuk melakukan perulangan selama node pada indeks tersebut masih ada.

`if current.key == key:` digunakan untuk mengecek apakah kode booking pada node saat ini sama dengan kode booking yang ingin dihapus.

`if prev is None:` digunakan untuk mengecek apakah node yang ingin dihapus berada di posisi paling awal.

`self.table[index] = current.next` digunakan untuk menghapus node pertama dengan cara menggantinya menggunakan node setelahnya.

`else:` digunakan jika node yang ingin dihapus bukan node pertama.

`prev.next = current.next` digunakan untuk menghubungkan node sebelumnya ke node setelah node yang dihapus.

`return True` digunakan untuk memberi tanda bahwa data tiket berhasil dihapus.

`prev = current` digunakan untuk menyimpan node saat ini sebagai node sebelumnya sebelum berpindah ke node selanjutnya.

`current = current.next` digunakan untuk berpindah ke node berikutnya.

`return False` digunakan jika data tiket dengan kode booking tersebut tidak ditemukan.

**BAGIAN 7. BAGIAN FUNGSI DISPLAY:**

`def display(self):` digunakan untuk menampilkan seluruh isi hash table tiket bioskop.

`print("\nIsi Hash Table Tiket Bioskop:")` digunakan untuk menampilkan judul output ketika isi hash table ditampilkan.

`for i in range(self.SIZE):` digunakan untuk melakukan perulangan dari indeks pertama sampai indeks terakhir pada hash table.

`print(f"{i}: ", end="")` digunakan untuk menampilkan nomor indeks hash table. Perintah `end=""` digunakan agar output berikutnya tetap berada pada baris yang sama.

`current = self.table[i]` digunakan untuk mengambil node pertama pada indeks ke-i.

`while current is not None:` digunakan untuk menampilkan seluruh node yang ada pada indeks tersebut.

`print(f"({current.key}, {current.value}) -> ", end="")` digunakan untuk menampilkan kode booking dan data tiket pada node saat ini.

`current = current.next` digunakan untuk berpindah ke node berikutnya.

`print("NONE")` digunakan untuk menandai bahwa tidak ada lagi node setelah data terakhir pada indeks tersebut.

**BAGIAN 8. BAGIAN FUNGSI MAIN:**

`def main():` digunakan untuk membuat fungsi utama yang menjalankan program.

`hashmap = HashMapSeparateChaining()` digunakan untuk membuat objek hash map baru dari class HashMapSeparateChaining.

`while True:` digunakan untuk membuat perulangan menu agar program terus berjalan sampai user memilih keluar.

`print("\n=== SISTEM PENCARIAN TIKET BIOSKOP ===")` digunakan untuk menampilkan judul menu utama program.

`print("1. Tambah Data Tiket")` digunakan untuk menampilkan pilihan menu menambahkan data tiket.

`print("2. Cari Data Tiket")` digunakan untuk menampilkan pilihan menu mencari data tiket.

`print("3. Hapus Data Tiket")` digunakan untuk menampilkan pilihan menu menghapus data tiket.

`print("4. Tampilkan Semua Data")` digunakan untuk menampilkan pilihan menu melihat seluruh data tiket.

`print("5. Keluar")` digunakan untuk menampilkan pilihan menu keluar dari program.

`pilihan = input("Pilih menu: ")` digunakan untuk meminta user memilih menu yang ingin dijalankan.

**BAGIAN 9. BAGIAN TAMBAH DATA TIKET:**

`if pilihan == "1":` digunakan untuk menjalankan menu tambah data tiket jika user memilih angka 1.

`key = int(input("Masukkan kode booking: "))` digunakan untuk meminta user memasukkan kode booking. Nilai tersebut diubah menjadi integer karena digunakan sebagai key pada hash table.

`nama = input("Masukkan nama pembeli: ")` digunakan untuk meminta user memasukkan nama pembeli tiket.

`film = input("Masukkan judul film: ")` digunakan untuk meminta user memasukkan judul film yang ditonton.

`jam = input("Masukkan jam tayang: ")` digunakan untuk meminta user memasukkan jam tayang film.

`studio = input("Masukkan studio: ")` digunakan untuk meminta user memasukkan nomor atau nama studio.

`kursi = input("Masukkan nomor kursi: ")` digunakan untuk meminta user memasukkan nomor kursi penonton.

`value = f"{nama} | {film} | {jam} | {studio} | Kursi {kursi}"` digunakan untuk menggabungkan seluruh data tiket menjadi satu teks yang akan disimpan sebagai value.

`hashmap.insert(key, value)` digunakan untuk memasukkan kode booking dan data tiket ke dalam hash table.

`print("Data tiket berhasil ditambahkan.")` digunakan untuk menampilkan pesan bahwa data tiket berhasil disimpan.

**BAGIAN 10. BAGIAN CARI DATA TIKET:**

`elif pilihan == "2":` digunakan untuk menjalankan menu cari data tiket jika user memilih angka 2.

`key = int(input("Masukkan kode booking yang dicari: "))` digunakan untuk meminta user memasukkan kode booking yang ingin dicari.

`hasil = hashmap.search(key)` digunakan untuk mencari data tiket berdasarkan kode booking yang dimasukkan.

`if hasil is not None:` digunakan untuk mengecek apakah data tiket berhasil ditemukan.

`print("\nData tiket ditemukan!")` digunakan untuk menampilkan pesan bahwa data tiket ditemukan.

`print(f"Kode Booking : {hasil.key}")` digunakan untuk menampilkan kode booking dari data tiket yang ditemukan.

`print(f"Data Tiket   : {hasil.value}")` digunakan untuk menampilkan isi data tiket yang ditemukan.

`else:` digunakan jika data tiket tidak ditemukan.

`print("Data tiket tidak ditemukan.")` digunakan untuk menampilkan pesan bahwa kode booking tidak ada di dalam hash table.

**BAGIAN 11. BAGIAN HAPUS DATA TIKET:**

`elif pilihan == "3":` digunakan untuk menjalankan menu hapus data tiket jika user memilih angka 3.

`key = int(input("Masukkan kode booking yang ingin dihapus: "))` digunakan untuk meminta user memasukkan kode booking yang ingin dihapus.

`if hashmap.remove_key(key):` digunakan untuk menjalankan proses penghapusan data berdasarkan kode booking.

`print("Data tiket berhasil dihapus.")` digunakan untuk menampilkan pesan jika data tiket berhasil dihapus.

`else:` digunakan jika data tiket dengan kode booking tersebut tidak ditemukan.

`print("Data tiket tidak ditemukan.")` digunakan untuk menampilkan pesan bahwa data tiket gagal dihapus karena tidak ada di dalam hash table.

**BAGIAN 12. BAGIAN TAMPILKAN DATA DAN KELUAR:**

`elif pilihan == "4":` digunakan untuk menjalankan menu tampilkan semua data jika user memilih angka 4.

`hashmap.display()` digunakan untuk menampilkan seluruh isi hash table tiket bioskop.

`elif pilihan == "5":` digunakan untuk menjalankan menu keluar jika user memilih angka 5.

`print("Program selesai.")` digunakan untuk menampilkan pesan bahwa program telah selesai dijalankan.

`break` digunakan untuk menghentikan perulangan menu sehingga program berhenti.

`else:` digunakan jika user memasukkan pilihan selain angka 1 sampai 5.

`print("Pilihan tidak valid.")` digunakan untuk menampilkan pesan bahwa pilihan menu yang dimasukkan salah.

**BAGIAN 13. BAGIAN PEMANGGILAN PROGRAM:**

`if __name__ == "__main__":` digunakan untuk memastikan bahwa fungsi main hanya dijalankan ketika file Python ini dijalankan secara langsung.

`main()` digunakan untuk memanggil fungsi utama agar program sistem pencarian tiket bioskop dapat berjalan.


**D. Output Program :** <img width="715" height="392" alt="Screenshot 2026-06-09 201827" src="https://github.com/user-attachments/assets/a799382b-9152-4743-948a-e64d7d2c056d" /> 
User memilih menu 1 untuk menambahkan data tiket bioskop ke dalam sistem. Pada output tersebut, user memasukkan kode booking 23, nama pembeli agus, judul film dilan, jam tayang 14.00, studio 2, dan nomor kursi 1. Setelah semua data dimasukkan, program menampilkan pesan “Data tiket berhasil ditambahkan.” yang berarti data tiket berhasil disimpan ke dalam hash table. Dalam program ini, kode booking 23 digunakan sebagai key, sedangkan data tiket yang berisi nama, film, jam tayang, studio, dan kursi digunakan sebagai value. Karena menggunakan Hash Map Separate Chaining, kode booking tersebut akan diproses oleh fungsi hash untuk menentukan indeks penyimpanan data.

<img width="597" height="385" alt="Screenshot 2026-06-09 201953" src="https://github.com/user-attachments/assets/7dfe5b6b-b34d-4b47-b271-09f4b028c9b1" />
User memilih menu 1 untuk menambahkan data tiket bioskop ke dalam sistem. Pada output tersebut, user memasukkan kode booking 12, nama pembeli azhari, judul film ayah ini arahnya ke mana, jam tayang 16.00, studio 4, dan nomor kursi 3. Setelah semua data dimasukkan, program menampilkan pesan “Data tiket berhasil ditambahkan.” yang berarti data tiket berhasil disimpan ke dalam hash table. Dalam program ini, kode booking 12 digunakan sebagai key, sedangkan data tiket yang berisi nama pembeli, judul film, jam tayang, studio, dan nomor kursi digunakan sebagai value. Karena menggunakan Hash Map Separate Chaining, kode booking tersebut akan diproses oleh fungsi hash untuk menentukan indeks penyimpanan data.

<img width="547" height="387" alt="Screenshot 2026-06-09 202001" src="https://github.com/user-attachments/assets/85cc5ed6-dc70-4c70-8d53-3493c323e022" />
User memilih menu 1 untuk menambahkan data tiket bioskop ke dalam sistem. Pada output tersebut, user memasukkan kode booking 32, nama pembeli anhar, judul film dilan 1998, jam tayang 20.00, studio 2, dan nomor kursi 4. Setelah semua data dimasukkan, program menampilkan pesan “Data tiket berhasil ditambahkan.” yang berarti data tiket berhasil disimpan ke dalam hash table. Dalam program ini, kode booking 32 digunakan sebagai key, sedangkan data tiket yang berisi nama pembeli, judul film, jam tayang, studio, dan nomor kursi digunakan sebagai value. Karena menggunakan Hash Map Separate Chaining, kode booking tersebut akan diproses oleh fungsi hash untuk menentukan indeks penyimpanan data.

<img width="847" height="351" alt="Screenshot 2026-06-09 202009" src="https://github.com/user-attachments/assets/f12ed513-1489-4e5a-b741-d966f9ef9996" />
User memilih menu 2 untuk mencari data tiket bioskop berdasarkan kode booking. Pada output tersebut, user memasukkan kode booking 12, lalu program berhasil menemukan data tiket yang sesuai dan menampilkan pesan “Data tiket ditemukan!”. Data yang ditampilkan adalah kode booking 12 dengan nama pembeli azhari, judul film ayah ini arahnya ke mana, jam tayang 16.00, studio 4, dan kursi 3. Hal ini menunjukkan bahwa proses pencarian menggunakan Hash Map Separate Chaining berjalan dengan baik, karena program dapat menemukan data tiket berdasarkan key berupa kode booking yang sebelumnya sudah disimpan di dalam hash table.

<img width="618" height="260" alt="Screenshot 2026-06-09 202031" src="https://github.com/user-attachments/assets/906e60d8-8d92-40ce-991a-f4b2267f02ed" />
User memilih menu 3 untuk menghapus data tiket bioskop berdasarkan kode booking. Pada output tersebut, user memasukkan kode booking 32 sebagai data yang ingin dihapus, lalu program menampilkan pesan “Data tiket berhasil dihapus.” Hal ini menunjukkan bahwa data tiket dengan kode booking 32 sebelumnya sudah tersimpan di dalam hash table dan berhasil ditemukan oleh program. Setelah ditemukan, data tersebut dihapus menggunakan fungsi `remove_key`, sehingga kode booking 32 tidak lagi tersimpan di dalam sistem pencarian tiket bioskop.

<img width="814" height="505" alt="Screenshot 2026-06-09 202047" src="https://github.com/user-attachments/assets/1fd02c06-8b41-46a9-97be-af8a94ccca06" />
User memilih menu 4 untuk menampilkan seluruh data tiket bioskop yang tersimpan di dalam hash table. Pada output tersebut, program menampilkan isi hash table dari indeks 0 sampai 9. Data dengan kode booking 12 tersimpan pada indeks 2 karena hasil dari 12 % 10 adalah 2, sedangkan data dengan kode booking 23 tersimpan pada indeks 3 karena hasil dari 23 % 10 adalah 3. Data dengan kode booking 32 sudah tidak muncul karena sebelumnya telah dihapus dari sistem. Indeks lainnya menampilkan `NONE`, yang berarti tidak ada data tiket yang tersimpan pada indeks tersebut.

<img width="542" height="220" alt="Screenshot 2026-06-09 202056" src="https://github.com/user-attachments/assets/f3b4cd8b-8b03-4a7c-84f2-99aa2d2b46de" />
User memilih menu 5 untuk keluar dari program sistem pencarian tiket bioskop. Setelah pilihan tersebut dimasukkan, program menampilkan pesan “Program selesai.” yang berarti perulangan menu dihentikan dan program tidak lagi menerima input dari user. Bagian ini menunjukkan bahwa fitur keluar pada program berjalan dengan baik karena perintah `break` berhasil menghentikan proses menu utama.


**E. Link YouTube :**
