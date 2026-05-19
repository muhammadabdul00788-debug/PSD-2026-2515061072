class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, nama, film, jumlah_tiket):
        if self.is_full():
            print("Antrean penuh")
            return

        data = {
            "nama": nama,
            "film": film,
            "jumlah_tiket": jumlah_tiket
        }

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = data
        print(f"Pembeli {nama} berhasil masuk antrean")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        data = self.q[self.front_idx]
        print(f"Pembeli {data['nama']} sedang dilayani")
        print(f"Film: {data['film']}")
        print(f"Jumlah tiket: {data['jumlah_tiket']}")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        data = self.q[self.front_idx]
        print("Pembeli paling depan:")
        print(f"Nama: {data['nama']}")
        print(f"Film: {data['film']}")
        print(f"Jumlah tiket: {data['jumlah_tiket']}")

    def display(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print("Daftar antrean pembeli tiket bioskop:")
        i = self.front_idx
        nomor = 1

        while True:
            data = self.q[i]
            print(f"{nomor}. Nama: {data['nama']} | Film: {data['film']} | Tiket: {data['jumlah_tiket']}")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN
            nomor += 1


def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTREAN TIKET BIOSKOP ===")
        print("1. Tambah antrean pembeli")
        print("2. Layani pembeli")
        print("3. Lihat pembeli paling depan")
        print("4. Tampilkan semua antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Nama pembeli: ")
            film = input("Judul film: ")

            try:
                jumlah_tiket = int(input("Jumlah tiket: "))
                queue.enqueue(nama, film, jumlah_tiket)
            except ValueError:
                print("Jumlah tiket harus angka!")

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()