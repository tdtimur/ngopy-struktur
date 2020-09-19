class Kendaraan:
    def __init__(self, roda, bbm, lebar):
        self.roda = roda
        self.bbm = bbm
        self.lebar = lebar

    def masuk(self, jalan):
        if jalan.ditutup:
            return "Jalan ditutup"
        if self.lebar > jalan.lebar:
            return "Kendaraan terlalu lebar"
        else:
            return "Berhasil masuk"
