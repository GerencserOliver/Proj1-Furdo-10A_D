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

    @property
    def kello_id(self) -> int:
        kello_id: int = 306
        return kello_id

    @property
    def legtovabb_furdo(self) -> int:
        egy_ember_idoi: list[int] = []
        legnagyobb_ido: int = 0
        legkisebb_ido: int = 10000000
        for f in self.furdok:
            if f.azonosito == self.kello_id:
                egy_ember_idoi.append(f.rekord_ideje_mp)
                for e in self.furdok:
                    if e.rekord_ideje_mp in egy_ember_idoi:
                        if e.rekord_ideje_mp > legnagyobb_ido:
                            legnagyobb_ido = e.rekord_ideje_mp
                for k in self.furdok:
                    if k.rekord_ideje_mp in egy_ember_idoi:
                        if k.rekord_ideje_mp < legkisebb_ido:
                            legkisebb_ido = k.rekord_ideje_mp
        egy_ember_ideje: int = legnagyobb_ido - legkisebb_ido
        return egy_ember_ideje

    @property
    def legtovabb_oraban(self) -> float:
        legt_oraban: float = self.legtovabb_furdo // 3600
        return legt_oraban

    @property
    def legtovabb_percben(self) -> float:
        legt_percben: float = (self.legtovabb_furdo - self.legtovabb_oraban * 3600) // 60
        return legt_percben

    @property
    def legtovabb_mpben(self) -> float:
        legt_mpben: float = (self.legtovabb_furdo - (self.legtovabb_oraban * 3600 + self.legtovabb_percben * 60))
        return legt_mpben

    @property
    def azonosito_lista(self) -> list[int]:
        id_lista: list[int] = []
        for f in self.furdok:
            if f.azonosito not in id_lista:
                id_lista.append(f.azonosito)
        return id_lista

    @property
    def kello_azonosito(self) -> int:
        for f in self.azonosito_lista:
            if f == self.kello_id:
                return f

    def kiiras_oraban(self, vendeg: Furdo) -> str:
        return f'{vendeg.ki_ora}:{vendeg.ki_perc}:{vendeg.ki_mp}'

    def vendegek(self) -> int:
        furdo_helyek: list[int] = []
        ketto_hasznalatos_vendeg: int = 0
        elozo_vendeg: Furdo = self.furdok[0]
        for vendeg in self.furdok:
            if elozo_vendeg.azonosito != vendeg.azonosito:
                if len(furdo_helyek) == 2:
                    ketto_hasznalatos_vendeg += 1
                furdo_helyek.clear()
            if vendeg.furdo_azonosito not in furdo_helyek:
                furdo_helyek.append(vendeg.furdo_azonosito)
            elozo_vendeg = vendeg
        return ketto_hasznalatos_vendeg

    def __init__(self, forras: str):
        self.furdok = []
        with open(forras, 'r', encoding='utf-8')as file:
            for sor in file.read().splitlines():
                self.furdok.append(Furdo(sor))
