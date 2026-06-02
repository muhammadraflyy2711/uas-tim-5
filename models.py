from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):

    def __init__(self, kode, judul):
        self.__kode = kode
        self.__judul = judul
        self.__status = "Tersedia"

    def get_kode(self):
        return self.__kode

    def get_judul(self):
        return self.__judul

    def set_judul(self, judul):
        self.__judul = judul

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    @abstractmethod
    def tampilkan_info(self):
        pass


class Buku(ItemPerpustakaan):

    def __init__(self, kode, judul, penulis):
        super().__init__(kode, judul)
        self.__penulis = penulis

    def get_penulis(self):
        return self.__penulis

    def tampilkan_info(self):
        return [
            self.get_kode(),
            self.get_judul(),
            self.__penulis,
            self.get_status()
        ]


class Anggota:

    def __init__(self, id_anggota, nama):
        self.__id = id_anggota
        self.__nama = nama

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama