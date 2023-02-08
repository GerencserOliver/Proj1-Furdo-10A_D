class Furdo:
    _azonosito: int
    _furdo_azonosito: int
    _be_ki_lepett: int
    _ki_ora: int
    _ki_perc: int
    _ki_mp: int

    @property
    def azonosito(self) -> int:
        return self._azonosito

    @property
    def furdo_azonosito(self) -> int:
        return self._furdo_azonosito

    @property
    def rekord_ideje_mp(self) -> int:
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
    def be_ki_lepett(self) -> int:
        return self._be_ki_lepett

    def __init__(self, sor: str):
        azonosito, furdo_azonosito, be_ki, ki_ora, ki_perc, ki_mp = sor.split(' ')
        self._azonosito = int(azonosito)
        self._furdo_azonosito = int(furdo_azonosito)
        self._be_ki_lepett = int(be_ki)
        self._ki_ora = int(ki_ora)
        self._ki_perc = int(ki_perc)
        self._ki_mp = int(ki_mp)
