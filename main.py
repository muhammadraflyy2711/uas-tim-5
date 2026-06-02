from service import Perpustakaan

USERNAME = "admin"
PASSWORD = "123"


def login():

    print("=" * 50)
    print("      SISTEM PERPUSTAKAAN DIGITAL")
    print("=" * 50)

    user = input("Username : ")
    pw = input("Password : ")

    return user == USERNAME and pw == PASSWORD


def menu():

    perpus = Perpustakaan()

    while True:

        print("\n")
        print("=" * 50)
        print("MENU UTAMA")
        print("=" * 50)

        print("1. Tambah Buku")
        print("2. Daftar Buku")
        print("3. Cari Buku")
        print("4. Edit Buku")
        print("5. Hapus Buku")
        print("6. Tambah Anggota")
        print("7. Daftar Anggota")
        print("8. Pinjam Buku")
        print("9. Kembalikan Buku")
        print("10. Riwayat Peminjaman")
        print("11. Laporan")
        print("0. Keluar")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            perpus.tambah_buku()

        elif pilih == "2":
            perpus.tampilkan_buku()

        elif pilih == "3":
            perpus.cari_buku()

        elif pilih == "4":
            perpus.edit_buku()

        elif pilih == "5":
            perpus.hapus_buku()

        elif pilih == "6":
            perpus.tambah_anggota()

        elif pilih == "7":
            perpus.tampilkan_anggota()

        elif pilih == "8":
            perpus.pinjam_buku()

        elif pilih == "9":
            perpus.kembalikan_buku()

        elif pilih == "10":
            perpus.tampilkan_riwayat()

        elif pilih == "11":
            perpus.laporan()

        elif pilih == "0":
            print("\nTerima kasih...")
            break

        else:
            print("\nMenu tidak tersedia")


if login():
    menu()
else:
    print("\nLogin gagal")