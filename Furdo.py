class Furdo:
    atjaro: int
    oltozo: int
    uszoda: int
    szaunak: int
    gyogyvizes_medencek: int
    strand: int

    def __init__(self, sor: str):
        at, olt, usz, sza, gy_med, st = sor.split(' ')
        self.atjaro = int(at)
        self.oltozo = int(olt)
        self.sza = int(usz)
        self.szaunak = int(sza)
        self.gyogyvizes_medencek = int(gy_med)
        self.strand = int(st)