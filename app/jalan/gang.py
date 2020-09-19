from .jalan import Jalan


class Gang(Jalan):
    def __init__(self, lebar, buntu=False):
        super().__init__(lebar=lebar)
        self.buntu = buntu
