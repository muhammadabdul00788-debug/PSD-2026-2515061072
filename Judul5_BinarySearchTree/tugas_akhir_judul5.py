class Node:
    def __init__(self, nomor_kursi):
        self.key = nomor_kursi
        self.left = None
        self.right = None


class BSTKursiBioskop:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nomor_kursi):
        if root is None:
            return Node(nomor_kursi)

        if nomor_kursi < root.key:
            root.left = self.insert_node(root.left, nomor_kursi)
        elif nomor_kursi > root.key:
            root.right = self.insert_node(root.right, nomor_kursi)

        return root

    def insert(self, nomor_kursi):
        self.root = self.insert_node(self.root, nomor_kursi)

    def search_node(self, root, nomor_kursi):
        if root is None:
            return False

        if root.key == nomor_kursi:
            return True

        if nomor_kursi < root.key:
            return self.search_node(root.left, nomor_kursi)

        return self.search_node(root.right, nomor_kursi)

    def search(self, nomor_kursi):
        return self.search_node(self.root, nomor_kursi)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return

        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return -1

        current = root
        while current.left is not None:
            current = current.left

        return current.key

    def find_max(self, root):
        if root is None:
            return -1

        current = root
        while current.right is not None:
            current = current.right

        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0

        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    bst = BSTKursiBioskop()
    pilih = 0

    while pilih != 10:
        print("\n=== SISTEM NOMOR KURSI BIOSKOP ===")
        print("1. Masukkan nomor kursi")
        print("2. Cari nomor kursi")
        print("3. Tampilkan kursi secara Inorder")
        print("4. Tampilkan kursi secara Preorder")
        print("5. Tampilkan kursi secara Postorder")
        print("6. Nomor kursi terkecil")
        print("7. Nomor kursi terbesar")
        print("8. Hitung jumlah kursi")
        print("9. Jumlah seluruh nomor kursi")
        print("10. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue

        if pilih == 1:
            try:
                nomor = int(input("Masukkan nomor kursi: "))
                bst.insert(nomor)
                print(f"Nomor kursi {nomor} berhasil dimasukkan.")
            except ValueError:
                print("Input tidak valid! Masukkan angka.")

        elif pilih == 2:
            try:
                nomor = int(input("Cari nomor kursi: "))
                if bst.search(nomor):
                    print(f"Nomor kursi {nomor} ditemukan.")
                else:
                    print(f"Nomor kursi {nomor} tidak ditemukan.")
            except ValueError:
                print("Input tidak valid! Masukkan angka.")

        elif pilih == 3:
            print("Urutan kursi Inorder: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Urutan kursi Preorder: ", end="")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Urutan kursi Postorder: ", end="")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            hasil = bst.find_min(bst.root)
            if hasil == -1:
                print("Data kursi masih kosong.")
            else:
                print(f"Nomor kursi terkecil: {hasil}")

        elif pilih == 7:
            hasil = bst.find_max(bst.root)
            if hasil == -1:
                print("Data kursi masih kosong.")
            else:
                print(f"Nomor kursi terbesar: {hasil}")

        elif pilih == 8:
            print(f"Jumlah kursi yang tersimpan: {bst.count_nodes(bst.root)}")

        elif pilih == 9:
            print(f"Jumlah seluruh nomor kursi: {bst.sum_nodes(bst.root)}")

        elif pilih == 10:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()