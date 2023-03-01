class Furdo:
    _furdozo_azonosito: int
    _furdohelyseg_azonosito: int
    _be_ki_lepett: int
    _ki_ora: int
    _ki_perc: int
    _ki_mp: int

    @property
    def furdozo_azonosito(self) -> int:
        return self._furdozo_azonosito

    @property
    def furdohelyseg_azonosito(self) -> int:
        return self._furdohelyseg_azonosito

    @property
    def idopont_mpben(self) -> int:
        return self.ki_ora * 3600 + self.ki_perc * 60 + self.ki_mp

    @property
    def ki_ora(self) -> int:
        return self._ki_ora

    @property
    def ki_perc(self) -> int:
        return self._ki_perc

    @property
    def ki_mp(self) -> int:
        return self._ki_mp

    @property
    def be_ki_lepett(self) -> bool:
        if self._be_ki_lepett == 1:
            return False
        else:
            return True

    def __init__(self, sor: str):
        furdozo_azonosito, furdohelyseg_azonosito, be_ki, ki_ora, ki_perc, ki_mp = sor.split(' ')
        self._furdozo_azonosito = int(furdozo_azonosito)
        self._furdohelyseg_azonosito = int(furdohelyseg_azonosito)
        self._be_ki_lepett = int(be_ki)
        self._ki_ora = int(ki_ora)
        self._ki_perc = int(ki_perc)
        self._ki_mp = int(ki_mp)
