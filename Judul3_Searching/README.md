## Implementasi Sequential Search pada studi kasus Pencarian Data Film Bioskop



































BAGIAN 1. BAGIAN FUNGSI SEQUENTIAL SEARCH:

`def sequential_search(data, n, target):` digunakan untuk membuat fungsi bernama `sequential_search`. Fungsi ini memiliki tiga parameter, yaitu `data`, `n`, dan `target`. Parameter `data` digunakan untuk menerima list yang berisi data-data film bioskop, parameter `n` digunakan untuk menerima jumlah data film, sedangkan parameter `target` digunakan untuk menerima judul film yang ingin dicari oleh pengguna.

`i = 0` digunakan untuk membuat variabel `i` dengan nilai awal 0. Variabel `i` digunakan sebagai indeks awal untuk melakukan pengecekan data film dari posisi pertama. Karena indeks pada list Python dimulai dari 0, maka proses pencarian juga dimulai dari indeks ke-0.

`counter = 0` digunakan untuk membuat variabel `counter` dengan nilai awal 0. Variabel `counter` digunakan untuk menghitung berapa kali judul film yang dicari ditemukan di dalam data. Nilai awalnya adalah 0 karena sebelum proses pencarian dilakukan, belum ada data film yang ditemukan.

`while i < n` digunakan untuk melakukan perulangan selama nilai `i` masih lebih kecil dari jumlah data film. Perulangan ini menjadi inti dari algoritma Sequential Search, karena program akan memeriksa data satu per satu dari indeks awal sampai indeks terakhir.

`if data[i]["judul"].lower() == target.lower()` digunakan untuk membandingkan judul film pada indeks ke-`i` dengan judul film yang dicari oleh pengguna. Penggunaan `lower()` bertujuan agar pencarian tidak membedakan huruf besar dan huruf kecil. Dengan begitu, input seperti `avatar`, `Avatar`, atau `AVATAR` tetap dianggap sama.

`counter += 1` digunakan untuk menambahkan nilai `counter` sebanyak 1 apabila judul film yang dicari berhasil ditemukan.

`i += 1` digunakan untuk menambah nilai indeks agar program berpindah ke data film berikutnya sampai semua data selesai diperiksa.

`return counter` digunakan untuk mengembalikan jumlah film yang ditemukan kepada bagian utama program.

BAGIAN 2. BAGIAN FUNGSI UTAMA:

`def main():` digunakan untuk membuat fungsi utama yang mengatur jalannya program, mulai dari input jumlah data film, input detail film, menampilkan data film, sampai melakukan proses pencarian judul film.

`data = []` digunakan untuk membuat list kosong bernama `data`. List ini nantinya akan digunakan untuk menyimpan seluruh data film bioskop yang dimasukkan oleh pengguna.

BAGIAN 3. BAGIAN INPUT JUMLAH DATA FILM:

`while True` digunakan untuk membuat perulangan input jumlah data film. Perulangan ini bertujuan agar program terus meminta input sampai pengguna memasukkan nilai yang valid.

`try` digunakan untuk mencoba menjalankan perintah input yang memiliki kemungkinan error, terutama ketika pengguna diminta memasukkan angka.

`n = int(input("Masukkan jumlah data film: "))` digunakan untuk meminta pengguna memasukkan jumlah data film yang ingin disimpan. Fungsi `int()` digunakan untuk mengubah input pengguna menjadi tipe data integer.

`break` digunakan untuk menghentikan perulangan jika input yang dimasukkan benar berupa angka.

`except ValueError` akan dijalankan jika pengguna memasukkan input yang bukan angka. Bagian ini digunakan untuk menangani error ketika input tidak bisa diubah menjadi integer.

`print("Input tidak valid, silakan masukkan angka!")` digunakan untuk menampilkan pesan kesalahan kepada pengguna agar pengguna memasukkan input berupa angka.

BAGIAN 4. BAGIAN INPUT DATA FILM BIOSKOP:

`print("\nMasukkan data film bioskop:")` digunakan untuk menampilkan teks sebagai tanda bahwa pengguna akan mulai mengisi data film.

`for i in range(n)` digunakan untuk melakukan perulangan sebanyak jumlah data film yang telah dimasukkan oleh pengguna. Jika pengguna memasukkan 3 data film, maka perulangan ini akan berjalan sebanyak 3 kali.

`print(f"\nData film ke-{i + 1}")` digunakan untuk menampilkan urutan data film yang sedang diinput. Karena indeks pada Python dimulai dari 0, maka digunakan `i + 1` agar tampilan data dimulai dari angka 1.

`judul = input("Judul film  : ")` digunakan untuk meminta pengguna memasukkan judul film. Data judul film ini nantinya akan digunakan sebagai data utama dalam proses pencarian.

`studio = input("Studio      : ")` digunakan untuk meminta pengguna memasukkan nama studio tempat film ditayangkan.

`jam = input("Jam tayang  : ")` digunakan untuk meminta pengguna memasukkan jam tayang film.

BAGIAN 5. BAGIAN INPUT HARGA TIKET:

`while True` pada bagian input harga tiket digunakan agar pengguna harus memasukkan harga tiket dalam bentuk angka.

`try` digunakan untuk mencoba menjalankan proses input harga tiket.

`harga = int(input("Harga tiket : "))` digunakan untuk meminta pengguna memasukkan harga tiket. Fungsi `int()` digunakan agar harga tiket disimpan dalam bentuk angka atau integer.

`break` digunakan untuk menghentikan perulangan jika input harga tiket sudah benar berupa angka.

`except ValueError` akan dijalankan jika pengguna memasukkan harga yang bukan angka.

`print("Input tidak valid, silakan masukkan angka!")` digunakan untuk menampilkan pesan bahwa input harga tidak valid.

BAGIAN 6. BAGIAN PENYIMPANAN DATA FILM:

`data.append({...})` digunakan untuk menambahkan data film ke dalam list `data`. Data film disimpan dalam bentuk dictionary agar setiap informasi memiliki nama key masing-masing.

`"judul"` digunakan untuk menyimpan data judul film.

`"studio"` digunakan untuk menyimpan data studio tempat film ditayangkan.

`"jam"` digunakan untuk menyimpan data jam tayang film.

`"harga"` digunakan untuk menyimpan data harga tiket.

BAGIAN 7. BAGIAN MENAMPILKAN DATA FILM:

`print("\nData Film Bioskop:")` digunakan untuk menampilkan judul bagian daftar film yang telah dimasukkan oleh pengguna.

`for film in data` digunakan untuk mengambil setiap data film yang tersimpan di dalam list `data`. Setiap data film kemudian akan ditampilkan satu per satu.

`print(f"{film['judul']} - {film['studio']} - {film['jam']} - Rp{film['harga']}")` digunakan untuk menampilkan informasi film berupa judul, studio, jam tayang, dan harga tiket.

BAGIAN 8. BAGIAN INPUT JUDUL FILM YANG DICARI:

`target = input("\nMasukkan judul film yang ingin dicari: ")` digunakan untuk meminta pengguna memasukkan judul film yang ingin dicari.

`counter = sequential_search(data, n, target)` digunakan untuk memanggil fungsi `sequential_search`. Pada bagian ini, program mengirimkan data film, jumlah data film, dan judul film yang dicari ke dalam fungsi pencarian. Hasil pencarian kemudian disimpan ke dalam variabel `counter`.

BAGIAN 9. BAGIAN MENAMPILKAN HASIL PENCARIAN:

`if counter > 0` digunakan untuk mengecek apakah film yang dicari berhasil ditemukan. Jika nilai `counter` lebih dari 0, berarti film ditemukan di dalam data.

`print(f"\nFilm {target} ditemukan sebanyak {counter} kali.")` digunakan untuk menampilkan pesan bahwa film berhasil ditemukan beserta jumlah kemunculannya.

`else` akan dijalankan jika nilai `counter` tidak lebih dari 0. Bagian ini menunjukkan bahwa judul film yang dicari tidak ditemukan dalam data.

`print(f"\nFilm {target} tidak ditemukan.")` digunakan untuk menampilkan pesan bahwa film yang dicari tidak ada di dalam data film bioskop.

BAGIAN 10. BAGIAN MENJALANKAN PROGRAM:

`if __name__ == "__main__":` digunakan untuk memastikan bahwa fungsi `main()` hanya dijalankan ketika file Python dijalankan secara langsung.

`main()` digunakan untuk memanggil fungsi utama agar seluruh program dapat berjalan mulai dari input data sampai proses pencarian.
