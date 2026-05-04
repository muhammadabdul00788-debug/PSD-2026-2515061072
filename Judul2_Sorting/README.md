## Implementasi Insertion Sort pada studi kasus layanan antrian tiket bioskop

A. Judul Program : Implementasi Insertion Sort pada studi kasus layanan antrian tiket bioskop

B. Deskripsi Singkat : Program ini dibuat untuk mengurutkan data tiket bioskop berdasarkan harga tiket dari yang termurah sampai yang termahal. Setiap data yang dimasukkan oleh pengguna terdiri dari nama film dan harga tiket. Data tersebut kemudian disimpan ke dalam list, sehingga setiap film memiliki informasi harga yang dapat dibandingkan saat proses pengurutan dilakukan.

Algoritma yang digunakan adalah Insertion Sort, yaitu metode pengurutan yang bekerja dengan cara mengambil satu data, lalu menyisipkannya ke posisi yang sesuai pada bagian data yang sudah terurut. Pada program ini, proses perbandingan dilakukan berdasarkan harga tiket. Jika harga tiket sebelumnya lebih besar daripada harga tiket yang sedang diproses, maka data tersebut akan digeser ke kanan sampai posisi yang tepat ditemukan.

C. Source Code : <img width="1184" height="2506" alt="code-sorting" src="https://github.com/user-attachments/assets/16857913-f9b5-4686-8373-9fea7bbca25e" />

BAGIAN 1. BAGIAN FUNGSI INSERTION SORT: def insertion_sort(data_tiket, n): Baris ini digunakan untuk membuat fungsi bernama insertion_sort. Fungsi ini memiliki dua parameter, yaitu data_tiket sebagai list yang berisi nama film dan harga tiket, serta n sebagai jumlah data yang akan diurutkan. for i in range(1, n): Perulangan dimulai dari indeks ke-1 atau elemen kedua. temp = data_tiket[i]: Baris ini menyimpan data pada indeks ke-i ke dalam variabel sementara bernama temp. j = i - 1: Variabel j digunakan untuk menunjuk elemen sebelum data yang sedang diproses. while j >= 0 and data_tiket[j]["harga"] > temp["harga"]: Baris ini digunakan untuk membandingkan harga tiket sebelumnya dengan harga tiket yang sedang diproses. data_tiket[j + 1] = data_tiket[j]: Jika kondisi pada while terpenuhi, data pada posisi j dipindahkan ke posisi j + 1. j -= 1: Nilai j dikurangi satu agar proses perbandingan bisa lanjut ke elemen sebelumnya. data_tiket[j + 1] = temp: Setelah posisi yang tepat ditemukan, data yang disimpan di temp dimasukkan ke posisi tersebut.

BAGIAN 2. BAGIAN FUNGSI UTAMA: def main(): digunakan untuk membuat fungsi utama yang mengatur seluruh jalannya program. Baris try: digunakan untuk mencoba menjalankan input yang bisa menyebabkan error. Baris n = int(input("Masukkan jumlah film: ")) meminta user memasukkan jumlah film dan mengubahnya menjadi angka. Jika input bukan angka, maka except ValueError: akan dijalankan. Baris print("Input tidak valid!") menampilkan pesan kesalahan, sedangkan return menghentikan program agar tidak lanjut berjalan.

BAGIAN 3. BAGIAN PENYIMPANAN DATA: data_tiket = [] digunakan untuk membuat list kosong sebagai tempat menyimpan data nama film dan harga tiket. Baris print("\nMasukkan data tiket bioskop:") digunakan untuk menampilkan petunjuk bahwa user akan mulai memasukkan data tiket bioskop.

BAGIAN 4. BAGIAN INPUT NAMA FILM DAN HARGA TIKET: for i in range(n): digunakan agar user bisa memasukkan data sesuai jumlah film yang sudah ditentukan. Baris nama_film = input(f"Nama film ke-{i + 1}: ") meminta user memasukkan nama film, dan i + 1 membuat nomor film dimulai dari 1. Baris while True: digunakan supaya input harga terus diulang sampai benar. Di dalamnya, try: mengecek apakah input harga valid, lalu harga = int(input(f"Harga tiket film {nama_film}: ")) meminta harga tiket dan mengubahnya menjadi angka. Setelah itu, data_tiket.append({"nama_film": nama_film, "harga": harga}) menyimpan nama film dan harga tiket ke dalam list dalam bentuk dictionary. Jika harga sudah valid, break menghentikan perulangan input harga. Jika input bukan angka, except ValueError: akan berjalan dan print("Input tidak valid, silakan masukkan angka!") menampilkan pesan kesalahan.

BAGIAN 5. BAGIAN MENAMPILKAN DATA SEBELUM DIURUTKAN: print("\nData tiket sebelum diurutkan:") digunakan untuk menampilkan judul data sebelum proses sorting. Baris for tiket in data_tiket: mengambil setiap data tiket yang ada di dalam list. Kemudian print(f"{tiket['nama_film']} - Rp{tiket['harga']}") menampilkan nama film beserta harga tiket sebelum diurutkan.

BAGIAN 6. BAGIAN PROSES PENGURUTAN: insertion_sort(data_tiket, n) digunakan untuk memanggil fungsi Insertion Sort yang sudah dibuat sebelumnya.

BAGIAN 7. BAGIAN MENAMPILKAN HASIL AKHIR: print("\nData tiket setelah diurutkan dari harga termurah ke termahal:") digunakan untuk menampilkan judul hasil akhir setelah proses sorting. Baris for tiket in data_tiket: mengambil setiap data tiket yang sudah diurutkan. Kemudian print(f"{tiket['nama_film']} - Rp{tiket['harga']}") menampilkan nama film dan harga tiket dari harga termurah sampai termahal. 

BAGIAN 8. BAGIAN PEMANGGILAN PROGRAM: if __name__ == "__main__": digunakan untuk mengecek apakah file program dijalankan secara langsung. Jika benar, maka main() akan dipanggil untuk memulai seluruh proses program.

D. Output Program: 
<img width="743" height="598" alt="image" src="https://github.com/user-attachments/assets/65132b05-4467-46fc-b0e6-140c4baabb39" />

Jika user memasukkan jumlah film sebanyak 4, maka program akan meminta user untuk mengisi data film sebanyak empat kali. Pada contoh output tersebut, user memasukkan film pertama yaitu Jumbo dengan harga tiket Rp35000, film kedua yaitu Agak Laen dengan harga tiket Rp40000, film ketiga yaitu Dilan dengan harga tiket Rp55000, dan film keempat yaitu Ghost In the Cell dengan harga tiket Rp50000.

Setelah semua data dimasukkan, program menampilkan data tiket sebelum diurutkan sesuai urutan input dari user, yaitu Jumbo - Rp35000, Agak Laen - Rp40000, Dilan - Rp55000, dan Ghost In the Cell - Rp50000. Pada tahap ini data belum diurutkan, sehingga urutannya masih sama seperti saat user memasukkan data.

Kemudian program melakukan proses pengurutan menggunakan Insertion Sort berdasarkan harga tiket dari yang termurah sampai yang termahal. Setelah proses pengurutan selesai, data yang ditampilkan menjadi Jumbo - Rp35000, Agak Laen - Rp40000, Ghost In the Cell - Rp50000, dan Dilan - Rp55000. Dari hasil tersebut terlihat bahwa film Ghost In the Cell berpindah ke sebelum Dilan karena harga tiketnya Rp50000 lebih murah daripada harga tiket Dilan yang Rp55000.

E. Link YouTube : 
