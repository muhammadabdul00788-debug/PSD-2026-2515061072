class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return

            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nIsi Hash Table Tiket Bioskop:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NONE")


def main():
    hashmap = HashMapSeparateChaining()

    while True:
        print("\n=== SISTEM PENCARIAN TIKET BIOSKOP ===")
        print("1. Tambah Data Tiket")
        print("2. Cari Data Tiket")
        print("3. Hapus Data Tiket")
        print("4. Tampilkan Semua Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            key = int(input("Masukkan kode booking: "))
            nama = input("Masukkan nama pembeli: ")
            film = input("Masukkan judul film: ")
            jam = input("Masukkan jam tayang: ")
            studio = input("Masukkan studio: ")
            kursi = input("Masukkan nomor kursi: ")

            value = f"{nama} | {film} | {jam} | {studio} | Kursi {kursi}"
            hashmap.insert(key, value)

            print("Data tiket berhasil ditambahkan.")

        elif pilihan == "2":
            key = int(input("Masukkan kode booking yang dicari: "))
            hasil = hashmap.search(key)

            if hasil is not None:
                print("\nData tiket ditemukan!")
                print(f"Kode Booking : {hasil.key}")
                print(f"Data Tiket   : {hasil.value}")
            else:
                print("Data tiket tidak ditemukan.")

        elif pilihan == "3":
            key = int(input("Masukkan kode booking yang ingin dihapus: "))

            if hashmap.remove_key(key):
                print("Data tiket berhasil dihapus.")
            else:
                print("Data tiket tidak ditemukan.")

        elif pilihan == "4":
            hashmap.display()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()