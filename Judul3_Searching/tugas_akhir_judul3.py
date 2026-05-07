def sequential_search_sentinel(data, n, target):
    data.append({
        "judul": target,
        "studio": "",
        "jam": "",
        "harga": 0
    })

    i = 0

    while data[i]["judul"].lower() != target.lower():
        i += 1

    data.pop()

    if i < n:
        return True, i
    else:
        return False, -1


def main():
    data = []

    while True:
        try:
            n = int(input("Masukkan jumlah data film: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")

    print("\nMasukkan data film bioskop:")
    for i in range(n):
        print(f"\nData film ke-{i + 1}")

        judul = input("Judul film  : ")
        studio = input("Studio      : ")
        jam = input("Jam tayang  : ")

        while True:
            try:
                harga = int(input("Harga tiket : "))
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

        data.append({
            "judul": judul,
            "studio": studio,
            "jam": jam,
            "harga": harga
        })

    print("\nData Film Bioskop:")
    for film in data:
        print(f"{film['judul']} - {film['studio']} - {film['jam']} - Rp{film['harga']}")

    target = input("\nMasukkan judul film yang ingin dicari: ")

    found, index = sequential_search_sentinel(data, n, target)

    if found:
        print(f"\nFilm ditemukan pada indeks ke-{index}")
        print(f"Judul film : {data[index]['judul']}")
        print(f"Studio     : {data[index]['studio']}")
        print(f"Jam tayang : {data[index]['jam']}")
        print(f"Harga tiket: Rp{data[index]['harga']}")
    else:
        print(f"\nFilm {target} tidak ditemukan.")


if __name__ == "__main__":
    main()