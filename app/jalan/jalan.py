class Jalan:
    def __init__(self, lebar):
        self.lebar = lebar
        self.ditutup = False

    def tutup(self):
        self.ditutup = True

    def buka(self):
        self.ditutup = False
