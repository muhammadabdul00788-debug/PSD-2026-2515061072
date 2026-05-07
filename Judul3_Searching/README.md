## Implementasi Sequential Search Sentinel pada Pencarian Data Film Bioskop

**A. Judul Program :** 
Implementasi Sequential Search Sentinel pada studi kasus Pencarian Data Film Bioskop

**B. Deskripsi Singkat :**
Program ini merupakan implementasi algoritma Sequential Search Sentinel dalam studi kasus pencarian judul film pada sistem tiket bioskop. Program memungkinkan pengguna memasukkan data film seperti judul film, studio, jam tayang, dan harga tiket, kemudian pengguna dapat mencari judul film tertentu dari data yang telah dimasukkan.

Algoritma Sequential Search Sentinel digunakan dengan cara menambahkan data sementara sebagai penjaga di akhir list agar proses pencarian pasti berhenti. Metode ini tetap cocok digunakan pada data film bioskop yang belum terurut, karena pencarian dilakukan dari awal sampai data yang dicari ditemukan atau sampai mencapai data sentinel.

**C. Source Code :**
<img width="1170" height="3418" alt="code-searching2" src="https://github.com/user-attachments/assets/c0cb710a-a397-421b-b29d-c6e49e21c807" />





**BAGIAN 1. BAGIAN FUNGSI SEQUENTIAL SEARCH SENTINEL:**

`def sequential_search_sentinel(data, n, target):` digunakan untuk membuat fungsi bernama `sequential_search_sentinel`. Fungsi ini digunakan untuk mencari judul film pada data bioskop menggunakan algoritma Sequential Search Sentinel. Parameter `data` digunakan untuk menerima list data film, parameter `n` digunakan untuk menerima jumlah data film asli, sedangkan parameter `target` digunakan untuk menerima judul film yang ingin dicari oleh pengguna.

`data.append({ "judul": target, "studio": "", "jam": "", "harga": 0 })` digunakan untuk menambahkan data sementara di akhir list sebagai sentinel atau penjaga. Data ini dibuat dengan judul yang sama seperti target agar proses pencarian pasti berhenti ketika menemukan judul tersebut.

`"judul": target` digunakan untuk menyimpan judul film yang dicari sebagai data sentinel. Bagian ini menjadi pembanding utama saat proses pencarian berlangsung.

`"studio": ""` digunakan untuk mengisi data studio pada sentinel dengan string kosong, karena data ini hanya digunakan sebagai penjaga dan bukan data film asli.

`"jam": ""` digunakan untuk mengisi data jam tayang pada sentinel dengan string kosong, karena data sentinel tidak memerlukan jam tayang sebenarnya.

`"harga": 0` digunakan untuk mengisi harga tiket pada sentinel dengan nilai 0, karena data sentinel hanya bersifat sementara.

`i = 0` digunakan untuk membuat variabel `i` dengan nilai awal 0. Variabel ini digunakan sebagai indeks awal untuk melakukan pencarian dari data pertama.

`while data[i]["judul"].lower() != target.lower():` digunakan untuk melakukan perulangan selama judul film pada indeks ke-`i` tidak sama dengan judul film yang dicari. Proses ini akan terus berjalan sampai judul film ditemukan, baik pada data asli maupun pada data sentinel.

`data[i]["judul"]` digunakan untuk mengambil judul film dari data pada indeks ke-`i`.

`.lower()` digunakan agar pencarian tidak membedakan huruf besar dan huruf kecil. Dengan begitu, input seperti `avatar`, `Avatar`, atau `AVATAR` tetap dianggap sama.

`i += 1` digunakan untuk menambah nilai indeks agar program berpindah ke data berikutnya selama judul film belum ditemukan.

`data.pop()` digunakan untuk menghapus data sentinel yang sebelumnya ditambahkan di akhir list. Hal ini dilakukan agar data film kembali seperti semula dan tidak menyimpan data tambahan yang bukan data asli.

`if i < n:` digunakan untuk mengecek apakah indeks tempat data ditemukan masih berada dalam jumlah data asli. Jika nilai `i` lebih kecil dari `n`, berarti film ditemukan pada data asli.

`return True, i` digunakan untuk mengembalikan nilai `True` dan indeks film jika judul film ditemukan pada data asli.

`else:` digunakan jika kondisi `i < n` tidak terpenuhi. Artinya, judul film hanya ditemukan pada data sentinel, bukan pada data asli.

`return False, -1` digunakan untuk mengembalikan nilai `False` dan indeks `-1` jika judul film tidak ditemukan pada data asli.

**BAGIAN 2. BAGIAN FUNGSI UTAMA:**

`def main():` digunakan untuk membuat fungsi utama bernama `main`. Fungsi ini mengatur seluruh alur program, mulai dari input data film, menampilkan data film, sampai melakukan pencarian judul film.

`data = []` digunakan untuk membuat list kosong bernama `data`. List ini nantinya digunakan untuk menyimpan semua data film bioskop yang dimasukkan oleh pengguna.

**BAGIAN 3. BAGIAN INPUT JUMLAH DATA FILM:**

`while True:` digunakan untuk membuat perulangan agar program terus meminta input jumlah data film sampai pengguna memasukkan input yang valid.

`try:` digunakan untuk mencoba menjalankan perintah input yang memiliki kemungkinan error, terutama saat pengguna diminta memasukkan angka.

`n = int(input("Masukkan jumlah data film: "))` digunakan untuk meminta pengguna memasukkan jumlah data film yang ingin disimpan. Fungsi `int()` digunakan untuk mengubah input pengguna menjadi tipe data integer.

`break` digunakan untuk menghentikan perulangan jika input jumlah data film yang dimasukkan sudah benar berupa angka.

`except ValueError:` digunakan untuk menangani error jika pengguna memasukkan input yang bukan angka.

`print("Input tidak valid, silakan masukkan angka!")` digunakan untuk menampilkan pesan kesalahan agar pengguna memasukkan input berupa angka.

**BAGIAN 4. BAGIAN INPUT DATA FILM BIOSKOP:**

`print("\nMasukkan data film bioskop:")` digunakan untuk menampilkan teks sebagai tanda bahwa pengguna akan mulai memasukkan data film.

`for i in range(n):` digunakan untuk melakukan perulangan sebanyak jumlah data film yang telah dimasukkan oleh pengguna. Jika pengguna memasukkan 3 data film, maka perulangan ini akan berjalan sebanyak 3 kali.

`print(f"\nData film ke-{i + 1}")` digunakan untuk menampilkan urutan data film yang sedang dimasukkan. Karena indeks Python dimulai dari 0, maka digunakan `i + 1` agar tampilan dimulai dari angka 1.

`judul = input("Judul film  : ")` digunakan untuk meminta pengguna memasukkan judul film.

`studio = input("Studio      : ")` digunakan untuk meminta pengguna memasukkan nama studio tempat film ditayangkan.

`jam = input("Jam tayang  : ")` digunakan untuk meminta pengguna memasukkan jam tayang film.

**BAGIAN 5. BAGIAN INPUT HARGA TIKET:**

`while True:` pada bagian harga tiket digunakan agar program terus meminta input sampai pengguna memasukkan harga tiket dalam bentuk angka.

`try:` digunakan untuk mencoba menjalankan proses input harga tiket yang memiliki kemungkinan error.

`harga = int(input("Harga tiket : "))` digunakan untuk meminta pengguna memasukkan harga tiket. Fungsi `int()` digunakan agar harga tiket disimpan dalam bentuk angka atau integer.

`break` digunakan untuk menghentikan perulangan jika harga tiket yang dimasukkan sudah valid berupa angka.

`except ValueError:` digunakan untuk menangani error jika pengguna memasukkan harga tiket yang bukan angka.

`print("Input tidak valid, silakan masukkan angka!")` digunakan untuk menampilkan pesan bahwa input harga tiket tidak valid.

**BAGIAN 6. BAGIAN PENYIMPANAN DATA FILM:**

`data.append({` digunakan untuk menambahkan data film ke dalam list `data`.

`"judul": judul` digunakan untuk menyimpan judul film yang telah dimasukkan pengguna.

`"studio": studio` digunakan untuk menyimpan nama studio yang telah dimasukkan pengguna.

`"jam": jam` digunakan untuk menyimpan jam tayang film yang telah dimasukkan pengguna.

`"harga": harga` digunakan untuk menyimpan harga tiket yang telah dimasukkan pengguna.

`})` digunakan untuk menutup dictionary dan menyelesaikan proses penyimpanan satu data film ke dalam list.

**BAGIAN 7. BAGIAN MENAMPILKAN DATA FILM:**

`print("\nData Film Bioskop:")` digunakan untuk menampilkan judul bagian daftar film yang telah dimasukkan oleh pengguna.

`for film in data:` digunakan untuk mengambil setiap data film yang tersimpan di dalam list `data`.

`print(f"{film['judul']} - {film['studio']} - {film['jam']} - Rp{film['harga']}")` digunakan untuk menampilkan informasi film berupa judul, studio, jam tayang, dan harga tiket.

**BAGIAN 8. BAGIAN INPUT JUDUL FILM YANG DICARI:**

`target = input("\nMasukkan judul film yang ingin dicari: ")` digunakan untuk meminta pengguna memasukkan judul film yang ingin dicari.

`found, index = sequential_search_sentinel(data, n, target)` digunakan untuk memanggil fungsi `sequential_search_sentinel`. Fungsi ini akan mencari judul film berdasarkan data yang telah dimasukkan. Hasil pencarian disimpan dalam dua variabel, yaitu `found` dan `index`.

`found` digunakan untuk menyimpan status apakah film ditemukan atau tidak.

`index` digunakan untuk menyimpan posisi indeks film jika film ditemukan.

**BAGIAN 9. BAGIAN MENAMPILKAN HASIL PENCARIAN:**

`if found:` digunakan untuk mengecek apakah film berhasil ditemukan. Jika nilai `found` adalah `True`, maka program akan menampilkan detail film.

`print(f"\nFilm ditemukan pada indeks ke-{index}")` digunakan untuk menampilkan posisi indeks film yang berhasil ditemukan.

`print(f"Judul film : {data[index]['judul']}")` digunakan untuk menampilkan judul film yang ditemukan.

`print(f"Studio     : {data[index]['studio']}")` digunakan untuk menampilkan studio tempat film ditayangkan.

`print(f"Jam tayang : {data[index]['jam']}")` digunakan untuk menampilkan jam tayang film yang ditemukan.

`print(f"Harga tiket: Rp{data[index]['harga']}")` digunakan untuk menampilkan harga tiket film yang ditemukan.

`else:` digunakan jika nilai `found` adalah `False`. Artinya, film yang dicari tidak ditemukan pada data asli.

`print(f"\nFilm {target} tidak ditemukan.")` digunakan untuk menampilkan pesan bahwa film yang dicari tidak ditemukan.

**BAGIAN 10. BAGIAN MENJALANKAN PROGRAM:**

`if __name__ == "__main__":` digunakan untuk memastikan bahwa fungsi `main()` hanya dijalankan ketika file Python dijalankan secara langsung.

`main()` digunakan untuk memanggil fungsi utama agar program mulai berjalan.

**D. Output Program :**
<img width="638" height="889" alt="Screenshot 2026-05-07 173629" src="https://github.com/user-attachments/assets/d2998860-8f9d-489d-b328-30ac085bd3b3" />

Jika user memasukkan jumlah data film sebanyak 4, maka program akan meminta user untuk mengisi data film sebanyak empat kali. Pada contoh output tersebut, user memasukkan film pertama yaitu Dilan dengan studio 1, jam tayang 14.00, dan harga tiket Rp50000. Film kedua yaitu Ghost in the Cell dengan studio 3, jam tayang 16.00, dan harga tiket Rp40000. Film ketiga yaitu Mortal Kombat II dengan studio 4, jam tayang 13.00, dan harga tiket Rp45000. Film keempat yaitu Agak Laen dengan studio 5, jam tayang 20.00, dan harga tiket Rp60000.

Setelah semua data dimasukkan, program menampilkan kembali seluruh data film bioskop sesuai urutan input dari user. Data yang ditampilkan yaitu Dilan, Ghost in the Cell, Mortal Kombat II, dan Agak Laen. Pada tahap ini data belum dilakukan proses pencarian, program hanya menampilkan data film yang sudah disimpan agar user dapat memastikan bahwa data yang dimasukkan sudah benar.

<img width="756" height="190" alt="Screenshot 2026-05-07 173646" src="https://github.com/user-attachments/assets/92c86e4a-831c-43bc-8386-b53acfcc6755" />


Kemudian user memasukkan judul film yang ingin dicari, yaitu Mortal Kombat II. Program melakukan proses pencarian menggunakan Sequential Search Sentinel dengan cara memeriksa data film satu per satu dari awal sampai judul film yang dicari ditemukan. Dari hasil pencarian, film Mortal Kombat II ditemukan pada indeks ke-2. Setelah itu, program menampilkan detail film yang ditemukan, yaitu judul film Mortal Kombat II, studio 4, jam tayang 13.00, dan harga tiket Rp45000.


**E. Link YouTube :**
