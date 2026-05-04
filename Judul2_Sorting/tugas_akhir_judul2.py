def insertion_sort(data_tiket, n):
    for i in range(1, n):
        temp = data_tiket[i]
        j = i - 1

        while j >= 0 and data_tiket[j]["harga"] > temp["harga"]:
            data_tiket[j + 1] = data_tiket[j]
            j -= 1

        data_tiket[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah film: "))
    except ValueError:
        print("Input tidak valid!")
        return

    data_tiket = []

    print("\nMasukkan data tiket bioskop:")
    for i in range(n):
        nama_film = input(f"Nama film ke-{i + 1}: ")

        while True:
            try:
                harga = int(input(f"Harga tiket film {nama_film}: "))
                data_tiket.append({
                    "nama_film": nama_film,
                    "harga": harga
                })
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print("\nData tiket sebelum diurutkan:")
    for tiket in data_tiket:
        print(f"{tiket['nama_film']} - Rp{tiket['harga']}")

    insertion_sort(data_tiket, n)

    print("\nData tiket setelah diurutkan dari harga termurah ke termahal:")
    for tiket in data_tiket:
        print(f"{tiket['nama_film']} - Rp{tiket['harga']}")


if __name__ == "__main__":
    main()