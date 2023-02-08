from Furdo import Furdo


class Megoldas:
    furdok: list[Furdo]

    @property
    def elso_oltozo_kilepes(self) -> Furdo:
        elso_vendeg: Furdo = self.furdok[0]
        for adat in self.furdok:
            if adat.be_ki_lepett == 1 and adat.furdo_azonosito == 0:
                if elso_vendeg.rekord_ideje_mp > adat.rekord_ideje_mp:
                    elso_vendeg = adat
        return elso_vendeg

    @property
    def utolso_oltozo_kilepes(self) -> Furdo:
        utolso_vendeg: Furdo = self.furdok[0]
        for adat in self.furdok:
            if adat.be_ki_lepett == 1 and adat.furdo_azonosito == 0:
                if utolso_vendeg.rekord_ideje_mp < adat.rekord_ideje_mp:
                    utolso_vendeg = adat
        return utolso_vendeg

    def kiiras_oraban(self, vendeg: Furdo) -> str:
        return f'{vendeg.ki_ora}:{vendeg.ki_perc}:{vendeg.ki_mp}'

    def __init__(self, forras: str):
        self.furdok = []
        with open(forras, 'r', encoding='utf-8')as file:
            for sor in file.read().splitlines():
                self.furdok.append(Furdo(sor))
