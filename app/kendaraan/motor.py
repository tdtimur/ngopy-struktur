from .kendaraan import Kendaraan


class Motor(Kendaraan):
    def __init__(self, roda=2, bbm='bensin', lebar=1):
        super().__init__(roda, bbm, lebar)

    def paksa_masuk(self, jalan):
        if self.lebar >= jalan.lebar:
            return "Bisa dipaksa masuk"
