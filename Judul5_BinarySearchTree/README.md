## Implementasi Binary Search Tree pada Penyusunan Nomor Kursi Bioskop

**A. Judul Program :** Implementasi Binary Search Tree pada Penyusunan Nomor Kursi Bioskop

**B. Deskripsi Singkat :** Program ini merupakan implementasi Binary Search Tree (BST) dengan studi kasus sistem nomor kursi bioskop. Pada program ini, setiap nomor kursi disimpan sebagai node di dalam pohon. Nomor kursi yang lebih kecil akan ditempatkan di sebelah kiri, sedangkan nomor kursi yang lebih besar akan ditempatkan di sebelah kanan. Dengan konsep ini, data kursi dapat disusun secara terstruktur sehingga proses pencarian, penambahan, dan penampilan data menjadi lebih mudah dilakukan.

Program ini menyediakan beberapa menu utama, seperti memasukkan nomor kursi, mencari nomor kursi, menampilkan data kursi dengan metode inorder, preorder, dan postorder, mencari nomor kursi terkecil dan terbesar, menghitung jumlah kursi yang tersimpan, serta menjumlahkan seluruh nomor kursi. Program ini dibuat berdasarkan konsep BSTDasar, sehingga fitur yang digunakan masih berfokus pada operasi dasar Binary Search Tree dan cocok digunakan untuk memahami cara kerja struktur data pohon secara sederhana.

**C. Source Code :** <img width="724" height="2172" alt="ChatGPT Image 26 Mei 2026, 19 38 00" src="https://github.com/user-attachments/assets/f99f7a44-4660-49ec-a587-c394a2c3a3d1" />

**BAGIAN 1. BAGIAN CLASS NODE:**

`class Node:` digunakan untuk membuat class bernama Node. Class ini berfungsi sebagai tempat untuk membuat satu data atau satu simpul pada Binary Search Tree.

`def __init__(self, nomor_kursi):` digunakan sebagai constructor, yaitu fungsi yang otomatis berjalan ketika objek Node dibuat. Parameter `nomor_kursi` digunakan untuk menyimpan nilai nomor kursi yang dimasukkan user.

`self.key = nomor_kursi` digunakan untuk menyimpan nilai nomor kursi ke dalam variabel `key`. Jadi setiap node memiliki data utama berupa nomor kursi.

`self.left = None` digunakan untuk membuat anak kiri dari node. Nilai awalnya `None` karena saat node baru dibuat, node tersebut belum memiliki anak kiri.

`self.right = None` digunakan untuk membuat anak kanan dari node. Nilai awalnya `None` karena saat node baru dibuat, node tersebut belum memiliki anak kanan.

**BAGIAN 2. BAGIAN CLASS BSTKURSIBIOSKOP:**

`class BSTKursiBioskop:` digunakan untuk membuat class utama yang berisi semua proses Binary Search Tree pada sistem nomor kursi bioskop.

`def __init__(self):` digunakan sebagai constructor dari class BSTKursiBioskop. Fungsi ini otomatis berjalan saat objek BST dibuat.

`self.root = None` digunakan untuk membuat root atau akar pohon. Nilai awalnya `None` karena saat program baru dijalankan, data kursi masih kosong.

**BAGIAN 3. BAGIAN FUNGSI INSERT_NODE:**

`def insert_node(self, root, nomor_kursi):` digunakan untuk membuat fungsi yang bertugas memasukkan nomor kursi ke dalam Binary Search Tree. Parameter `root` digunakan sebagai posisi node yang sedang diperiksa, sedangkan `nomor_kursi` adalah data yang akan dimasukkan.

`if root is None:` digunakan untuk mengecek apakah posisi node saat ini masih kosong.

`return Node(nomor_kursi)` digunakan untuk membuat node baru jika posisi tersebut masih kosong. Node baru ini akan berisi nomor kursi yang dimasukkan user.

`if nomor_kursi < root.key:` digunakan untuk mengecek apakah nomor kursi yang dimasukkan lebih kecil dari nilai node saat ini.

`root.left = self.insert_node(root.left, nomor_kursi)` digunakan untuk memasukkan nomor kursi ke bagian kiri pohon jika nilainya lebih kecil dari node saat ini.

`elif nomor_kursi > root.key:` digunakan untuk mengecek apakah nomor kursi yang dimasukkan lebih besar dari nilai node saat ini.

`root.right = self.insert_node(root.right, nomor_kursi)` digunakan untuk memasukkan nomor kursi ke bagian kanan pohon jika nilainya lebih besar dari node saat ini.

`return root` digunakan untuk mengembalikan root setelah proses memasukkan data selesai, supaya struktur pohon tetap tersambung dengan benar.

**BAGIAN 4. BAGIAN FUNGSI INSERT:**

`def insert(self, nomor_kursi):` digunakan untuk membuat fungsi insert yang lebih sederhana agar bisa dipanggil saat user ingin memasukkan nomor kursi.

`self.root = self.insert_node(self.root, nomor_kursi)` digunakan untuk menjalankan proses insert mulai dari root utama. Hasilnya disimpan kembali ke `self.root` agar data yang baru dimasukkan masuk ke dalam pohon.

**BAGIAN 5. BAGIAN FUNGSI SEARCH_NODE:**

`def search_node(self, root, nomor_kursi):` digunakan untuk membuat fungsi pencarian nomor kursi di dalam Binary Search Tree. Parameter `root` adalah node yang sedang diperiksa, sedangkan `nomor_kursi` adalah data yang dicari.

`if root is None:` digunakan untuk mengecek apakah node saat ini kosong.

`return False` digunakan untuk mengembalikan nilai salah jika node kosong, artinya nomor kursi tidak ditemukan.

`if root.key == nomor_kursi:` digunakan untuk mengecek apakah nilai node saat ini sama dengan nomor kursi yang dicari.

`return True` digunakan untuk mengembalikan nilai benar jika nomor kursi berhasil ditemukan.

`if nomor_kursi < root.key:` digunakan untuk mengecek apakah nomor kursi yang dicari lebih kecil dari nilai node saat ini.

`return self.search_node(root.left, nomor_kursi)` digunakan untuk melanjutkan pencarian ke bagian kiri pohon jika nomor kursi lebih kecil.

`return self.search_node(root.right, nomor_kursi)` digunakan untuk melanjutkan pencarian ke bagian kanan pohon jika nomor kursi lebih besar.

**BAGIAN 6. BAGIAN FUNGSI SEARCH:**

`def search(self, nomor_kursi):` digunakan untuk membuat fungsi pencarian yang lebih sederhana agar bisa dipanggil dari menu program.

`return self.search_node(self.root, nomor_kursi)` digunakan untuk menjalankan proses pencarian mulai dari root utama.

**BAGIAN 7. BAGIAN FUNGSI INORDER:**

`def inorder(self, root):` digunakan untuk membuat fungsi traversal inorder, yaitu menampilkan data dengan urutan kiri, root, lalu kanan.

`if root is None:` digunakan untuk mengecek apakah node saat ini kosong.

`return` digunakan untuk menghentikan fungsi jika node kosong.

`self.inorder(root.left)` digunakan untuk membaca atau menampilkan data yang ada di bagian kiri terlebih dahulu.

`print(root.key, end=" ")` digunakan untuk menampilkan nilai node saat ini tanpa pindah baris.

`self.inorder(root.right)` digunakan untuk membaca atau menampilkan data yang ada di bagian kanan setelah root ditampilkan.

**BAGIAN 8. BAGIAN FUNGSI PREORDER:**

`def preorder(self, root):` digunakan untuk membuat fungsi traversal preorder, yaitu menampilkan data dengan urutan root, kiri, lalu kanan.

`if root is None:` digunakan untuk mengecek apakah node saat ini kosong.

`return` digunakan untuk menghentikan fungsi jika node kosong.

`print(root.key, end=" ")` digunakan untuk menampilkan nilai node saat ini terlebih dahulu.

`self.preorder(root.left)` digunakan untuk membaca atau menampilkan data yang ada di bagian kiri.

`self.preorder(root.right)` digunakan untuk membaca atau menampilkan data yang ada di bagian kanan.

**BAGIAN 9. BAGIAN FUNGSI POSTORDER:**

`def postorder(self, root):` digunakan untuk membuat fungsi traversal postorder, yaitu menampilkan data dengan urutan kiri, kanan, lalu root.

`if root is None:` digunakan untuk mengecek apakah node saat ini kosong.

`return` digunakan untuk menghentikan fungsi jika node kosong.

`self.postorder(root.left)` digunakan untuk membaca atau menampilkan data yang ada di bagian kiri terlebih dahulu.

`self.postorder(root.right)` digunakan untuk membaca atau menampilkan data yang ada di bagian kanan.

`print(root.key, end=" ")` digunakan untuk menampilkan nilai node saat ini setelah bagian kiri dan kanan selesai dibaca.

**BAGIAN 10. BAGIAN FUNGSI FIND_MIN:**

`def find_min(self, root):` digunakan untuk membuat fungsi mencari nomor kursi terkecil di dalam Binary Search Tree.

`if root is None:` digunakan untuk mengecek apakah pohon masih kosong.

`return -1` digunakan untuk memberi tanda bahwa tidak ada data jika pohon masih kosong.

`current = root` digunakan untuk membuat variabel `current` yang dimulai dari root.

`while current.left is not None:` digunakan untuk melakukan perulangan selama node saat ini masih memiliki anak kiri.

`current = current.left` digunakan untuk berpindah ke node kiri, karena dalam BST nilai terkecil selalu berada di bagian paling kiri.

`return current.key` digunakan untuk mengembalikan nilai paling kecil setelah node paling kiri ditemukan.

**BAGIAN 11. BAGIAN FUNGSI FIND_MAX:**

`def find_max(self, root):` digunakan untuk membuat fungsi mencari nomor kursi terbesar di dalam Binary Search Tree.

`if root is None:` digunakan untuk mengecek apakah pohon masih kosong.

`return -1` digunakan untuk memberi tanda bahwa tidak ada data jika pohon masih kosong.

`current = root` digunakan untuk membuat variabel `current` yang dimulai dari root.

`while current.right is not None:` digunakan untuk melakukan perulangan selama node saat ini masih memiliki anak kanan.

`current = current.right` digunakan untuk berpindah ke node kanan, karena dalam BST nilai terbesar selalu berada di bagian paling kanan.

`return current.key` digunakan untuk mengembalikan nilai paling besar setelah node paling kanan ditemukan.

**BAGIAN 12. BAGIAN FUNGSI COUNT_NODES:**

`def count_nodes(self, root):` digunakan untuk membuat fungsi menghitung jumlah node atau jumlah nomor kursi yang tersimpan.

`if root is None:` digunakan untuk mengecek apakah node saat ini kosong.

`return 0` digunakan untuk mengembalikan nilai 0 jika node kosong.

`return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)` digunakan untuk menghitung node saat ini ditambah jumlah node di kiri dan jumlah node di kanan.

**BAGIAN 13. BAGIAN FUNGSI SUM_NODES:**

`def sum_nodes(self, root):` digunakan untuk membuat fungsi menjumlahkan semua nomor kursi yang tersimpan dalam BST.

`if root is None:` digunakan untuk mengecek apakah node saat ini kosong.

`return 0` digunakan untuk mengembalikan nilai 0 jika node kosong.

`return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)` digunakan untuk menjumlahkan nilai node saat ini dengan semua nilai yang ada di bagian kiri dan kanan.

**BAGIAN 14. BAGIAN FUNGSI MAIN:**

`def main():` digunakan untuk membuat fungsi utama program. Semua proses menu dijalankan dari fungsi ini.

`bst = BSTKursiBioskop()` digunakan untuk membuat objek dari class BSTKursiBioskop. Objek ini dipakai untuk menjalankan insert, search, traversal, min, max, count, dan sum.

`pilih = 0` digunakan untuk memberi nilai awal pada variabel pilihan menu.

`while pilih != 10:` digunakan untuk membuat program terus berjalan selama user belum memilih menu 10.

**BAGIAN 15. BAGIAN TAMPILAN MENU:**

`print("\n=== SISTEM NOMOR KURSI BIOSKOP ===")` digunakan untuk menampilkan judul menu program.

`print("1. Masukkan nomor kursi")` digunakan untuk menampilkan menu memasukkan nomor kursi baru.

`print("2. Cari nomor kursi")` digunakan untuk menampilkan menu pencarian nomor kursi.

`print("3. Tampilkan kursi secara Inorder")` digunakan untuk menampilkan menu traversal inorder.

`print("4. Tampilkan kursi secara Preorder")` digunakan untuk menampilkan menu traversal preorder.

`print("5. Tampilkan kursi secara Postorder")` digunakan untuk menampilkan menu traversal postorder.

`print("6. Nomor kursi terkecil")` digunakan untuk menampilkan menu mencari nomor kursi paling kecil.

`print("7. Nomor kursi terbesar")` digunakan untuk menampilkan menu mencari nomor kursi paling besar.

`print("8. Hitung jumlah kursi")` digunakan untuk menampilkan menu menghitung jumlah nomor kursi yang tersimpan.

`print("9. Jumlah seluruh nomor kursi")` digunakan untuk menampilkan menu menjumlahkan semua nomor kursi.

`print("10. Keluar")` digunakan untuk menampilkan menu keluar dari program.

**BAGIAN 16. BAGIAN INPUT PILIHAN MENU:**

`try:` digunakan untuk mencoba menjalankan perintah input menu agar program tidak langsung error jika user salah memasukkan data.

`pilih = int(input("Pilih menu: "))` digunakan untuk meminta user memilih menu, lalu mengubah input tersebut menjadi tipe data integer.

`except ValueError:` digunakan untuk menangani error jika user memasukkan data yang bukan angka.

`print("Input tidak valid! Masukkan angka.")` digunakan untuk menampilkan pesan bahwa input user salah.

`continue` digunakan untuk mengulang program kembali ke tampilan menu utama.

**BAGIAN 17. BAGIAN MENU MASUKKAN NOMOR KURSI:**

`if pilih == 1:` digunakan untuk mengecek apakah user memilih menu nomor 1.

`try:` digunakan untuk mencoba menjalankan proses input nomor kursi agar tidak error jika input salah.

`nomor = int(input("Masukkan nomor kursi: "))` digunakan untuk meminta user memasukkan nomor kursi, lalu mengubah input menjadi integer.

`bst.insert(nomor)` digunakan untuk memasukkan nomor kursi ke dalam Binary Search Tree.

`print(f"Nomor kursi {nomor} berhasil dimasukkan.")` digunakan untuk menampilkan pesan bahwa nomor kursi berhasil disimpan.

`except ValueError:` digunakan untuk menangani error jika user memasukkan data yang bukan angka.

`print("Input tidak valid! Masukkan angka.")` digunakan untuk memberi tahu user bahwa input harus berupa angka.

**BAGIAN 18. BAGIAN MENU CARI NOMOR KURSI:**

`elif pilih == 2:` digunakan untuk mengecek apakah user memilih menu nomor 2.

`try:` digunakan untuk mencoba menjalankan proses pencarian nomor kursi.

`nomor = int(input("Cari nomor kursi: "))` digunakan untuk meminta user memasukkan nomor kursi yang ingin dicari.

`if bst.search(nomor):` digunakan untuk mengecek apakah nomor kursi ditemukan di dalam BST.

`print(f"Nomor kursi {nomor} ditemukan.")` digunakan untuk menampilkan pesan jika nomor kursi berhasil ditemukan.

`else:` digunakan jika nomor kursi tidak ditemukan.

`print(f"Nomor kursi {nomor} tidak ditemukan.")` digunakan untuk menampilkan pesan bahwa nomor kursi tidak ada di dalam BST.

`except ValueError:` digunakan untuk menangani error jika input bukan angka.

`print("Input tidak valid! Masukkan angka.")` digunakan untuk memberi tahu user bahwa input harus berupa angka.

**BAGIAN 19. BAGIAN MENU INORDER:**

`elif pilih == 3:` digunakan untuk mengecek apakah user memilih menu nomor 3.

`print("Urutan kursi Inorder: ", end="")` digunakan untuk menampilkan teks keterangan sebelum hasil inorder.

`bst.inorder(bst.root)` digunakan untuk menampilkan semua nomor kursi dengan urutan inorder, yaitu kiri, root, kanan.

`print()` digunakan untuk membuat baris baru setelah hasil inorder selesai ditampilkan.

**BAGIAN 20. BAGIAN MENU PREORDER:**

`elif pilih == 4:` digunakan untuk mengecek apakah user memilih menu nomor 4.

`print("Urutan kursi Preorder: ", end="")` digunakan untuk menampilkan teks keterangan sebelum hasil preorder.

`bst.preorder(bst.root)` digunakan untuk menampilkan semua nomor kursi dengan urutan preorder, yaitu root, kiri, kanan.

`print()` digunakan untuk membuat baris baru setelah hasil preorder selesai ditampilkan.

**BAGIAN 21. BAGIAN MENU POSTORDER:**

`elif pilih == 5:` digunakan untuk mengecek apakah user memilih menu nomor 5.

`print("Urutan kursi Postorder: ", end="")` digunakan untuk menampilkan teks keterangan sebelum hasil postorder.

`bst.postorder(bst.root)` digunakan untuk menampilkan semua nomor kursi dengan urutan postorder, yaitu kiri, kanan, root.

`print()` digunakan untuk membuat baris baru setelah hasil postorder selesai ditampilkan.

**BAGIAN 22. BAGIAN MENU NOMOR KURSI TERKECIL:**

`elif pilih == 6:` digunakan untuk mengecek apakah user memilih menu nomor 6.

`hasil = bst.find_min(bst.root)` digunakan untuk mencari nomor kursi terkecil yang tersimpan di dalam BST.

`if hasil == -1:` digunakan untuk mengecek apakah data kursi masih kosong.

`print("Data kursi masih kosong.")` digunakan untuk menampilkan pesan jika belum ada nomor kursi yang dimasukkan.

`else:` digunakan jika data kursi sudah ada.

`print(f"Nomor kursi terkecil: {hasil}")` digunakan untuk menampilkan nomor kursi terkecil.

**BAGIAN 23. BAGIAN MENU NOMOR KURSI TERBESAR:**

`elif pilih == 7:` digunakan untuk mengecek apakah user memilih menu nomor 7.

`hasil = bst.find_max(bst.root)` digunakan untuk mencari nomor kursi terbesar yang tersimpan di dalam BST.

`if hasil == -1:` digunakan untuk mengecek apakah data kursi masih kosong.

`print("Data kursi masih kosong.")` digunakan untuk menampilkan pesan jika belum ada nomor kursi yang dimasukkan.

`else:` digunakan jika data kursi sudah ada.

`print(f"Nomor kursi terbesar: {hasil}")` digunakan untuk menampilkan nomor kursi terbesar.

**BAGIAN 24. BAGIAN MENU HITUNG JUMLAH KURSI:**

`elif pilih == 8:` digunakan untuk mengecek apakah user memilih menu nomor 8.

`print(f"Jumlah kursi yang tersimpan: {bst.count_nodes(bst.root)}")` digunakan untuk menampilkan jumlah node atau jumlah nomor kursi yang sudah dimasukkan ke dalam BST.

**BAGIAN 25. BAGIAN MENU JUMLAH SELURUH NOMOR KURSI:**

`elif pilih == 9:` digunakan untuk mengecek apakah user memilih menu nomor 9.

`print(f"Jumlah seluruh nomor kursi: {bst.sum_nodes(bst.root)}")` digunakan untuk menampilkan hasil penjumlahan semua nomor kursi yang tersimpan di dalam BST.

**BAGIAN 26. BAGIAN MENU KELUAR:**

`elif pilih == 10:` digunakan untuk mengecek apakah user memilih menu nomor 10.

`print("Program selesai.")` digunakan untuk menampilkan pesan bahwa program telah selesai dijalankan.

**BAGIAN 27. BAGIAN PILIHAN TIDAK VALID:**

`else:` digunakan jika user memilih menu selain angka 1 sampai 10.

`print("Pilihan tidak valid!")` digunakan untuk menampilkan pesan bahwa pilihan menu yang dimasukkan tidak tersedia.

**BAGIAN 28. BAGIAN PEMANGGILAN PROGRAM:**

`if __name__ == "__main__":` digunakan untuk mengecek apakah file Python ini sedang dijalankan secara langsung.

`main()` digunakan untuk memanggil fungsi utama agar program mulai berjalan.


**D. Output Program :** <img width="806" height="787" alt="Screenshot 2026-05-26 193555" src="https://github.com/user-attachments/assets/95e9fcee-0962-4585-a933-50893844a1e3" />
User memilih menu 1 untuk memasukkan nomor kursi ke dalam sistem. Pada input pertama, user memasukkan nomor kursi 12 dan program menampilkan pesan “Nomor kursi 12 berhasil dimasukkan.” Setelah itu, user kembali memilih menu 1 dan memasukkan nomor kursi 13, lalu program menampilkan pesan “Nomor kursi 13 berhasil dimasukkan.” Karena program menggunakan konsep Binary Search Tree, nomor kursi 12 tersimpan terlebih dahulu sebagai data awal, sedangkan nomor kursi 13 ditempatkan di sebelah kanan karena nilainya lebih besar dari 12.

<img width="811" height="777" alt="Screenshot 2026-05-26 193614" src="https://github.com/user-attachments/assets/ce6e8c94-ab38-4764-836a-e077f9c84a00" />
User memilih menu 1 untuk memasukkan nomor kursi ke dalam sistem. Pada input pertama, user memasukkan nomor kursi 11 dan program menampilkan pesan “Nomor kursi 11 berhasil dimasukkan.” Setelah itu, user kembali memilih menu 1 dan memasukkan nomor kursi 7, lalu program menampilkan pesan “Nomor kursi 7 berhasil dimasukkan.” Karena program menggunakan konsep Binary Search Tree, nomor kursi 11 dan 7 akan disimpan sesuai aturan BST, yaitu nomor yang lebih kecil ditempatkan ke bagian kiri, sedangkan nomor yang lebih besar ditempatkan ke bagian kanan.

<img width="802" height="775" alt="Screenshot 2026-05-26 193628" src="https://github.com/user-attachments/assets/d6ab9e63-74c0-41b9-889b-d661c6a841e9" />
User memilih menu 1 untuk memasukkan nomor kursi ke dalam sistem. Pada input pertama, user memasukkan nomor kursi 6 dan program menampilkan pesan “Nomor kursi 6 berhasil dimasukkan.” Setelah itu, user kembali memilih menu 1 dan memasukkan nomor kursi 5, lalu program menampilkan pesan “Nomor kursi 5 berhasil dimasukkan.” Karena program menggunakan konsep Binary Search Tree, nomor kursi 6 tersimpan terlebih dahulu sebagai data awal, sedangkan nomor kursi 5 ditempatkan di sebelah kiri karena nilainya lebih kecil dari 6.

<img width="805" height="783" alt="Screenshot 2026-05-26 193646" src="https://github.com/user-attachments/assets/a476e9c8-c99e-4e33-b04c-187199b871e2" />
User memilih menu 1 untuk memasukkan nomor kursi baru, lalu user memasukkan nomor kursi 15 dan program menampilkan pesan “Nomor kursi 15 berhasil dimasukkan.” Setelah itu, user memilih menu 2 untuk mencari nomor kursi yang sudah tersimpan di dalam sistem. Pada bagian pencarian, user memasukkan nomor kursi 12, lalu program menampilkan pesan “Nomor kursi 12 ditemukan.” Hal ini menunjukkan bahwa nomor kursi 12 sebelumnya sudah berhasil disimpan di dalam Binary Search Tree, sehingga saat dicari program dapat menemukannya.

<img width="808" height="734" alt="Screenshot 2026-05-26 193701" src="https://github.com/user-attachments/assets/b5293011-9bbc-4555-8e96-92ee3eb2ddca" />
User memilih menu 3 untuk menampilkan data kursi secara inorder, lalu program menampilkan hasil “5 6 7 11 12 13 15”. Hasil tersebut menunjukkan bahwa traversal inorder pada Binary Search Tree menampilkan data dari nilai terkecil sampai nilai terbesar. Setelah itu, user memilih menu 4 untuk menampilkan data kursi secara preorder, lalu program menampilkan hasil “12 11 7 6 5 13 15”. Hasil preorder tersebut menampilkan data dengan urutan root terlebih dahulu, kemudian bagian kiri, lalu bagian kanan.

<img width="807" height="737" alt="Screenshot 2026-05-26 193717" src="https://github.com/user-attachments/assets/58e77ba3-42e6-42ef-ac9d-4e210d8c6cb9" />
User memilih menu 5 untuk menampilkan data kursi secara postorder, lalu program menampilkan hasil “5 6 7 11 15 13 12”. Hasil tersebut menunjukkan bahwa traversal postorder pada Binary Search Tree menampilkan data dengan urutan bagian kiri terlebih dahulu, kemudian bagian kanan, dan root ditampilkan paling akhir. Setelah itu, user memilih menu 6 untuk mencari nomor kursi terkecil, lalu program menampilkan hasil “Nomor kursi terkecil: 5” karena angka 5 merupakan nilai paling kecil yang tersimpan di dalam BST.


<img width="792" height="735" alt="Screenshot 2026-05-26 193733" src="https://github.com/user-attachments/assets/87b2aa1a-5a75-416f-83b7-4683d483be28" />
User memilih menu 7 untuk mencari nomor kursi terbesar, lalu program menampilkan hasil “Nomor kursi terbesar: 15” karena angka 15 merupakan nilai paling besar yang tersimpan di dalam Binary Search Tree. Setelah itu, user memilih menu 9 untuk menjumlahkan seluruh nomor kursi yang ada di dalam sistem, lalu program menampilkan hasil “Jumlah seluruh nomor kursi: 69”. Hasil tersebut berasal dari penjumlahan semua nomor kursi yang sudah tersimpan, yaitu 5 + 6 + 7 + 11 + 12 + 13 + 15.


<img width="805" height="351" alt="Screenshot 2026-05-26 193746" src="https://github.com/user-attachments/assets/6c8ed65a-d386-4596-92e3-3c5d211db16a" />
User memilih menu 10 yaitu keluar dari program, lalu program menampilkan pesan “Program selesai.” Hal ini menunjukkan bahwa sistem nomor kursi bioskop sudah dihentikan dan program tidak akan menjalankan menu lainnya lagi. Menu keluar digunakan untuk mengakhiri proses setelah user selesai memasukkan, mencari, atau menampilkan data nomor kursi yang tersimpan di dalam Binary Search Tree.


**E. Link YouTube :**
