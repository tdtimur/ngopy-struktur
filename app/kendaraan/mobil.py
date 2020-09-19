from .kendaraan import Kendaraan


class Mobil(Kendaraan):
    def __init__(self, roda=4, bbm='bensin', lebar=4):
        super().__init__(roda, bbm, lebar)

    def paksa_masuk(self, jalan):
        if self.lebar >= jalan.lebar:
            return "Tidak bisa dipaksa masuk"
