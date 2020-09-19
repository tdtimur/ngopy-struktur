from .jalan import Jalan


class Tol(Jalan):
    def __init__(self, lebar, macet=False):
        super().__init__(lebar=lebar)
        self.macet = macet
