from models import Buku, Anggota
from mixins import CetakMixin
from datetime import datetime


class Perpustakaan(CetakMixin):

    def __init__(self):
        self.daftar_buku = []
        self.daftar_anggota = []
        self.riwayat = []

    # =====================
    # BUKU
    # =====================

    def tambah_buku(self):

        kode = input("Kode Buku    : ")
        judul = input("Judul Buku   : ")
        penulis = input("Penulis      : ")

        self.daftar_buku.append(
            Buku(kode, judul, penulis)
        )

        print("\n✓ Buku berhasil ditambahkan")

    def tampilkan_buku(self):

        if not self.daftar_buku:
            print("\nBelum ada buku.")
            return

        self.garis()

        print(
            f"{'Kode':<10}"
            f"{'Judul':<25}"
            f"{'Penulis':<20}"
            f"{'Status'}"
        )

        self.garis()

        for buku in self.daftar_buku:

            data = buku.tampilkan_info()

            print(
                f"{data[0]:<10}"
                f"{data[1]:<25}"
                f"{data[2]:<20}"
                f"{data[3]}"
            )

        self.garis()

    def cari_buku(self):

        kode = input("Kode Buku : ")

        for buku in self.daftar_buku:

            if buku.get_kode() == kode:

                print("\nDATA DITEMUKAN")
                self.garis()

                data = buku.tampilkan_info()

                print("Kode     :", data[0])
                print("Judul    :", data[1])
                print("Penulis  :", data[2])
                print("Status   :", data[3])

                return

        print("Buku tidak ditemukan")

    def edit_buku(self):

        kode = input("Kode Buku : ")

        for buku in self.daftar_buku:

            if buku.get_kode() == kode:

                judul = input("Judul Baru : ")
                buku.set_judul(judul)

                print("✓ Data berhasil diubah")
                return

        print("Buku tidak ditemukan")

    def hapus_buku(self):

        kode = input("Kode Buku : ")

        for buku in self.daftar_buku:

            if buku.get_kode() == kode:

                self.daftar_buku.remove(buku)

                print("✓ Buku berhasil dihapus")
                return

        print("Buku tidak ditemukan")

    # =====================
    # ANGGOTA
    # =====================

    def tambah_anggota(self):

        id_anggota = input("ID Anggota : ")
        nama = input("Nama       : ")

        self.daftar_anggota.append(
            Anggota(id_anggota, nama)
        )

        print("✓ Anggota berhasil ditambahkan")

    def tampilkan_anggota(self):

        if not self.daftar_anggota:
            print("Belum ada anggota")
            return

        self.garis()

        print(
            f"{'ID':<15}"
            f"{'Nama'}"
        )

        self.garis()

        for anggota in self.daftar_anggota:

            print(
                f"{anggota.get_id():<15}"
                f"{anggota.get_nama()}"
            )

        self.garis()

    # =====================
    # PINJAM
    # =====================

    def pinjam_buku(self):

        kode = input("Kode Buku : ")
        nama = input("Nama Peminjam : ")

        for buku in self.daftar_buku:

            if buku.get_kode() == kode:

                if buku.get_status() == "Dipinjam":

                    print("Buku sedang dipinjam")
                    return

                buku.set_status("Dipinjam")

                self.riwayat.append({
                    "nama": nama,
                    "judul": buku.get_judul(),
                    "tanggal": datetime.now().strftime("%d-%m-%Y")
                })

                print("✓ Buku berhasil dipinjam")
                return

        print("Buku tidak ditemukan")

    def kembalikan_buku(self):

        kode = input("Kode Buku : ")

        for buku in self.daftar_buku:

            if buku.get_kode() == kode:

                buku.set_status("Tersedia")

                print("✓ Buku berhasil dikembalikan")
                return

        print("Buku tidak ditemukan")

    # =====================
    # RIWAYAT
    # =====================

    def tampilkan_riwayat(self):

        if not self.riwayat:
            print("Belum ada riwayat")
            return

        self.garis()

        print(
            f"{'Nama':<20}"
            f"{'Buku':<25}"
            f"{'Tanggal'}"
        )

        self.garis()

        for data in self.riwayat:

            print(
                f"{data['nama']:<20}"
                f"{data['judul']:<25}"
                f"{data['tanggal']}"
            )

        self.garis()

    # =====================
    # LAPORAN
    # =====================

    def laporan(self):

        total = len(self.daftar_buku)

        tersedia = sum(
            1 for buku in self.daftar_buku
            if buku.get_status() == "Tersedia"
        )

        dipinjam = total - tersedia

        self.garis()

        print("LAPORAN PERPUSTAKAAN")

        self.garis()

        print("Total Buku     :", total)
        print("Tersedia       :", tersedia)
        print("Dipinjam       :", dipinjam)
        print("Total Anggota  :", len(self.daftar_anggota))

        self.garis()