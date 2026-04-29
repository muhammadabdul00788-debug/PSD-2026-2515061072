class Node:
    def __init__(self, nama, film, jumlah_tiket):
        self.nama = nama
        self.film = film
        self.jumlah_tiket = jumlah_tiket
        self.next = None


class AntrianTiketBioskop:
    def __init__(self):
        self.front = None   
        self.rear = None    

    def tambah_antrian(self, nama, film, jumlah_tiket):
        new_node = Node(nama, film, jumlah_tiket)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"{nama} berhasil masuk ke antrian.")

    def layani_antrian(self):
        if self.front is None:
            print("Antrian kosong, belum ada pembeli tiket.")
        else:
            pembeli = self.front

            print("\nPembeli yang dilayani:")
            print(f"Nama         : {pembeli.nama}")
            print(f"Film         : {pembeli.film}")
            print(f"Jumlah Tiket : {pembeli.jumlah_tiket}")

            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print(f"{pembeli.nama} telah selesai dilayani.")

    def tampilkan_antrian(self):
        if self.front is None:
            print("Antrian masih kosong.")
        else:
            current = self.front
            nomor = 1

            print("\nDaftar Antrian Tiket Bioskop:")
            while current is not None:
                print(f"{nomor}. {current.nama}, Film: {current.film}, Tiket: {current.jumlah_tiket}")
                current = current.next
                nomor += 1

    def hitung_antrian(self):
        current = self.front
        total = 0

        while current is not None:
            total += 1
            current = current.next

        print(f"Jumlah orang dalam antrian: {total}")


def menu():
    print("SISTEM ANTRIAN TIKET BIOSKOP")
    print("1. Tambah Antrian")
    print("2. Layani Pembeli")
    print("3. Tampilkan Antrian")
    print("4. Hitung Jumlah Antrian")
    print("5. Keluar")


def main():
    antrian = AntrianTiketBioskop()

    while True:
        menu()

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == 1:
            nama = input("Masukkan nama pembeli: ")
            film = input("Masukkan judul film: ")

            try:
                jumlah_tiket = int(input("Masukkan jumlah tiket: "))
            except ValueError:
                print("Jumlah tiket harus berupa angka!")
                continue

            antrian.tambah_antrian(nama, film, jumlah_tiket)

        elif pilihan == 2:
            antrian.layani_antrian()

        elif pilihan == 3:
            antrian.tampilkan_antrian()

        elif pilihan == 4:
            antrian.hitung_antrian()

        elif pilihan == 5:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()