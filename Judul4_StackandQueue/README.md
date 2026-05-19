# Implementasi QueueArray pada Antrian Tiket Bioskop 

**A. Judul Program** : Implementasi QueueArray pada studi kasus Antrian Tiket Bioskop  
  
**B. Deskripsi Singkat** : Program ini merupakan implementasi struktur data Queue Array dengan study case sistem antrean tiket bioskop. Program dibuat menggunakan bahasa Python dan menerapkan konsep FIFO (First In First Out), yaitu pembeli yang pertama masuk antrean akan menjadi pembeli pertama yang dilayani. Dalam program ini terdapat beberapa operasi utama seperti menambahkan antrean pembeli (enqueue), melayani antrean pembeli (dequeue), melihat antrean paling depan (peek), dan menampilkan seluruh antrean pembeli (display).

Program menggunakan array/list sebagai media penyimpanan data antrean dengan bantuan variabel `front_idx` dan `rear_idx` untuk mengatur posisi depan dan belakang queue. Selain itu, program juga menerapkan konsep circular queue agar penggunaan array lebih efisien. Setiap data pembeli yang masuk akan menyimpan informasi berupa nama pembeli, judul film, dan jumlah tiket yang dibeli sehingga program dapat mensimulasikan sistem antrean pada bioskop secara sederhana.

**C. Source Code** : <img width="1186" height="5508" alt="code-snapshot4" src="https://github.com/user-attachments/assets/752b8639-3b78-4867-b3c7-f4679b868bab" />

**BAGIAN 1. BAGIAN CLASS QUEUE ARRAY:**

`class QueueArray:` digunakan untuk membuat class bernama `QueueArray` yang berfungsi sebagai sistem antrean tiket bioskop menggunakan Queue Array.

`def __init__(self, max_size=100):` digunakan untuk membuat constructor atau fungsi awal yang otomatis dijalankan saat object queue dibuat.

`self` digunakan untuk merepresentasikan object dari class itu sendiri.

`max_size=100` digunakan untuk memberikan nilai default kapasitas maksimum queue sebanyak 100 data.

`self.MAXN = max_size` digunakan untuk menyimpan kapasitas maksimum queue ke dalam variabel `MAXN`.

`self.q = [None] * self.MAXN` digunakan untuk membuat list kosong sebanyak kapasitas queue yang sudah ditentukan.

`[None]` digunakan sebagai isi awal list yang masih kosong.

`* self.MAXN` digunakan untuk mengulang nilai `None` sesuai kapasitas maksimum queue.

`self.front_idx = -1` digunakan untuk menandai posisi depan queue. Nilai `-1` berarti queue masih kosong.

`self.rear_idx = -1` digunakan untuk menandai posisi belakang queue. Nilai `-1` berarti queue masih kosong.

**BAGIAN 2. BAGIAN FUNGSI IS EMPTY:**

`def is_empty(self):` digunakan untuk membuat fungsi pengecekan apakah queue kosong atau tidak.

`return self.front_idx == -1` digunakan untuk mengembalikan nilai `True` jika queue kosong karena `front_idx` bernilai `-1`.

`return` digunakan untuk mengembalikan hasil dari fungsi.

`==` digunakan sebagai operator perbandingan.

`-1` digunakan sebagai penanda queue kosong.

**BAGIAN 3. BAGIAN FUNGSI IS FULL:**

`def is_full(self):` digunakan untuk membuat fungsi pengecekan apakah queue penuh.

`return (self.rear_idx + 1) % self.MAXN == self.front_idx` digunakan untuk memeriksa apakah posisi belakang queue sudah bertemu posisi depan queue.

`self.rear_idx + 1` digunakan untuk menghitung posisi belakang berikutnya.

`% self.MAXN` digunakan untuk membuat queue menjadi circular queue atau berputar.

`== self.front_idx` digunakan untuk membandingkan apakah posisi belakang berikutnya sudah sama dengan posisi depan.

**BAGIAN 4. BAGIAN FUNGSI ENQUEUE:**

`def enqueue(self, nama, film, jumlah_tiket):` digunakan untuk membuat fungsi menambahkan pembeli ke dalam antrean bioskop.

`nama` digunakan untuk menerima input nama pembeli.

`film` digunakan untuk menerima input judul film.

`jumlah_tiket` digunakan untuk menerima input jumlah tiket pembeli.

`if self.is_full():` digunakan untuk memeriksa apakah queue sudah penuh.

`if` digunakan untuk menjalankan kondisi percabangan.

`self.is_full()` digunakan untuk memanggil fungsi pengecekan queue penuh.

`print("Antrean penuh")` digunakan untuk menampilkan pesan bahwa queue sudah penuh.

`print` digunakan untuk menampilkan output ke layar.

`return` digunakan untuk menghentikan proses enqueue jika queue penuh.

`data = {` digunakan untuk membuat dictionary data pembeli.

`"nama": nama` digunakan untuk menyimpan nama pembeli ke dalam dictionary.

`:` digunakan untuk memisahkan key dan value pada dictionary.

`"film": film` digunakan untuk menyimpan judul film ke dalam dictionary.

`"jumlah_tiket": jumlah_tiket` digunakan untuk menyimpan jumlah tiket pembeli.

`}` digunakan untuk menutup dictionary.

`if self.is_empty():` digunakan untuk memeriksa apakah queue masih kosong.

`self.is_empty()` digunakan untuk memanggil fungsi pengecekan queue kosong.

`self.front_idx = 0` digunakan untuk mengatur posisi depan queue menjadi indeks pertama.

`0` digunakan sebagai indeks pertama pada list.

`self.rear_idx = 0` digunakan untuk mengatur posisi belakang queue menjadi indeks pertama.

`else:` digunakan jika queue tidak kosong.

`self.rear_idx = (self.rear_idx + 1) % self.MAXN` digunakan untuk memindahkan posisi belakang queue ke indeks berikutnya secara circular.

`(self.rear_idx + 1)` digunakan untuk menambah posisi belakang satu langkah.

`% self.MAXN` digunakan agar indeks kembali ke awal jika sudah mencapai batas maksimum queue.

`self.q[self.rear_idx] = data` digunakan untuk menyimpan data pembeli ke posisi belakang queue.

`self.q` digunakan untuk memanggil list queue.

`[self.rear_idx]` digunakan untuk menentukan indeks penyimpanan data.

`= data` digunakan untuk memasukkan data pembeli ke queue.

`print(f"Pembeli {nama} berhasil masuk antrean")` digunakan untuk menampilkan pesan bahwa pembeli berhasil masuk antrean.

`f""` digunakan sebagai format string agar variabel bisa dipanggil di dalam teks.

`{nama}` digunakan untuk menampilkan isi variabel nama.

**BAGIAN 5. BAGIAN FUNGSI DEQUEUE:**

`def dequeue(self):` digunakan untuk membuat fungsi melayani atau menghapus pembeli paling depan dari antrean.

`if self.is_empty():` digunakan untuk memeriksa apakah queue kosong.

`print("Antrean kosong")` digunakan untuk menampilkan pesan bahwa queue kosong.

`return` digunakan untuk menghentikan fungsi dequeue jika queue kosong.

`data = self.q[self.front_idx]` digunakan untuk mengambil data pembeli paling depan.

`self.front_idx` digunakan untuk menunjukkan posisi depan queue.

`print(f"Pembeli {data['nama']} sedang dilayani")` digunakan untuk menampilkan nama pembeli yang sedang dilayani.

`data['nama']` digunakan untuk mengambil nama pembeli dari dictionary.

`print(f"Film: {data['film']}")` digunakan untuk menampilkan judul film pembeli.

`data['film']` digunakan untuk mengambil data film dari dictionary.

`print(f"Jumlah tiket: {data['jumlah_tiket']}")` digunakan untuk menampilkan jumlah tiket pembeli.

`data['jumlah_tiket']` digunakan untuk mengambil jumlah tiket dari dictionary.

`if self.front_idx == self.rear_idx:` digunakan untuk memeriksa apakah queue hanya memiliki satu data.

`self.front_idx = -1` digunakan untuk mengembalikan posisi depan menjadi kosong.

`self.rear_idx = -1` digunakan untuk mengembalikan posisi belakang menjadi kosong.

`else:` digunakan jika queue masih memiliki data lain.

`self.front_idx = (self.front_idx + 1) % self.MAXN` digunakan untuk memindahkan posisi depan queue ke data berikutnya.

`(self.front_idx + 1)` digunakan untuk menambah posisi depan satu langkah.

**BAGIAN 6. BAGIAN FUNGSI PEEK:**

`def peek(self):` digunakan untuk membuat fungsi melihat data paling depan tanpa menghapusnya.

`if self.is_empty():` digunakan untuk memeriksa apakah queue kosong.

`print("Antrean kosong")` digunakan untuk menampilkan pesan bahwa queue kosong.

`return` digunakan untuk menghentikan fungsi peek jika queue kosong.

`data = self.q[self.front_idx]` digunakan untuk mengambil data paling depan queue.

`print("Pembeli paling depan:")` digunakan untuk menampilkan informasi antrean paling depan.

`print(f"Nama: {data['nama']}")` digunakan untuk menampilkan nama pembeli paling depan.

`print(f"Film: {data['film']}")` digunakan untuk menampilkan film pembeli paling depan.

`print(f"Jumlah tiket: {data['jumlah_tiket']}")` digunakan untuk menampilkan jumlah tiket pembeli paling depan.

**BAGIAN 7. BAGIAN FUNGSI DISPLAY:**

`def display(self):` digunakan untuk membuat fungsi menampilkan seluruh data antrean.

`if self.is_empty():` digunakan untuk memeriksa apakah queue kosong.

`print("Antrean kosong")` digunakan untuk menampilkan pesan queue kosong.

`return` digunakan untuk menghentikan fungsi display jika queue kosong.

`print("Daftar antrean pembeli tiket bioskop:")` digunakan untuk menampilkan judul daftar antrean.

`i = self.front_idx` digunakan untuk memulai perulangan dari posisi depan queue.

`nomor = 1` digunakan untuk membuat nomor urut antrean.

`while True:` digunakan untuk membuat perulangan tanpa batas sampai ditemukan perintah berhenti.

`while` digunakan untuk membuat perulangan.

`True` digunakan agar perulangan terus berjalan.

`data = self.q[i]` digunakan untuk mengambil data queue berdasarkan indeks `i`.

`print(f"{nomor}. Nama: {data['nama']} | Film: {data['film']} | Tiket: {data['jumlah_tiket']}")` digunakan untuk menampilkan seluruh data pembeli.

`{nomor}` digunakan untuk menampilkan nomor antrean.

`|` digunakan sebagai pemisah tampilan output.

`if i == self.rear_idx:` digunakan untuk memeriksa apakah indeks sudah mencapai antrean paling belakang.

`break` digunakan untuk menghentikan perulangan.

`i = (i + 1) % self.MAXN` digunakan untuk berpindah ke indeks berikutnya secara circular.

`nomor += 1` digunakan untuk menambah nomor antrean satu per satu.

`+=` digunakan sebagai operator penambahan langsung.

**BAGIAN 8. BAGIAN FUNGSI MAIN:**

`def main():` digunakan untuk membuat fungsi utama program.

`queue = QueueArray()` digunakan untuk membuat object queue dari class `QueueArray`.

`QueueArray()` digunakan untuk memanggil class QueueArray.

`pilih = 0` digunakan untuk menyimpan pilihan menu pengguna.

`while pilih != 5:` digunakan untuk menjalankan menu terus menerus selama pengguna belum memilih menu keluar.

`!=` digunakan sebagai operator tidak sama dengan.

`print("\n=== SISTEM ANTREAN TIKET BIOSKOP ===")` digunakan untuk menampilkan judul menu program.

`\n` digunakan untuk membuat baris baru.

`print("1. Tambah antrean pembeli")` digunakan untuk menampilkan menu tambah antrean.

`print("2. Layani pembeli")` digunakan untuk menampilkan menu melayani pembeli.

`print("3. Lihat pembeli paling depan")` digunakan untuk menampilkan menu melihat antrean depan.

`print("4. Tampilkan semua antrean")` digunakan untuk menampilkan menu menampilkan semua antrean.

`print("5. Keluar")` digunakan untuk menampilkan menu keluar.

`try:` digunakan untuk mencoba menjalankan kode yang berpotensi error.

`pilih = int(input("Pilih: "))` digunakan untuk menerima input pilihan menu dari pengguna.

`input()` digunakan untuk menerima input dari keyboard.

`int()` digunakan untuk mengubah input menjadi integer.

`except ValueError:` digunakan untuk menangani error jika input bukan angka.

`ValueError` digunakan untuk error akibat input tidak sesuai tipe data.

`print("Input tidak valid!")` digunakan untuk menampilkan pesan kesalahan input.

`continue` digunakan untuk mengulang kembali perulangan menu.

`if pilih == 1:` digunakan untuk menjalankan menu tambah antrean.

`nama = input("Nama pembeli: ")` digunakan untuk menerima input nama pembeli.

`film = input("Judul film: ")` digunakan untuk menerima input judul film.

`jumlah_tiket = int(input("Jumlah tiket: "))` digunakan untuk menerima input jumlah tiket dalam bentuk angka.

`queue.enqueue(nama, film, jumlah_tiket)` digunakan untuk menambahkan data pembeli ke queue.

`elif pilih == 2:` digunakan untuk menjalankan menu melayani pembeli.

`queue.dequeue()` digunakan untuk menghapus atau melayani antrean paling depan.

`elif pilih == 3:` digunakan untuk menjalankan menu melihat antrean depan.

`queue.peek()` digunakan untuk melihat data antrean paling depan.

`elif pilih == 4:` digunakan untuk menjalankan menu menampilkan seluruh antrean.

`queue.display()` digunakan untuk menampilkan seluruh isi queue.

`elif pilih == 5:` digunakan untuk menjalankan menu keluar program.

`print("Program selesai.")` digunakan untuk menampilkan pesan program selesai.

`else:` digunakan jika pilihan menu tidak tersedia.

`print("Pilihan tidak valid!")` digunakan untuk menampilkan pesan pilihan salah.

**BAGIAN 9. BAGIAN PEMANGGIL PROGRAM:**

`if __name__ == "__main__":` digunakan untuk memastikan program utama hanya berjalan saat file dijalankan langsung.

`__name__` merupakan variabel bawaan Python.

`"__main__"` menandakan file sedang dijalankan langsung.

`main()` digunakan untuk memanggil fungsi utama program.

**D. Output Program** :


