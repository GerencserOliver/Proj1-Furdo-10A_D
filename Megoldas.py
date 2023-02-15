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

    @property
    def bent_voltak_szama_uszoda(self) -> int:
        uszodaban_voltak: list[int] = []
        for f in self.furdok:
            if f.azonosito not in uszodaban_voltak:
                if f.furdo_azonosito == 1:
                    uszodaban_voltak.append(f.azonosito)
        return len(uszodaban_voltak)

    @property
    def bent_voltak_szama_szauna(self) -> int:
        szaunaban_voltak: list[int] = []
        for f in self.furdok:
            if f.azonosito not in szaunaban_voltak:
                if f.furdo_azonosito == 2:
                    szaunaban_voltak.append(f.azonosito)
        return len(szaunaban_voltak)

    @property
    def bent_voltak_szama_gyogymeddence(self) -> int:
        gyogyfurdoben_voltak: list[int] = []
        for f in self.furdok:
            if f.azonosito not in gyogyfurdoben_voltak:
                if f.furdo_azonosito == 3:
                    gyogyfurdoben_voltak.append(f.azonosito)
        return len(gyogyfurdoben_voltak)

    @property
    def bent_voltak_szama_strand(self) -> int:
        strandon_voltak: list[int] = []
        for f in self.furdok:
            if f.azonosito not in strandon_voltak:
                if f.furdo_azonosito == 4:
                    strandon_voltak.append(f.azonosito)
        return len(strandon_voltak)

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

    @property
    def vendegek_erkezes(self) -> list[int]:
        hat_kilenc: int = 0
        kilenc_tizenhat: int = 0
        tizenhat_husz: int = 0
        elso_alkalom: list[int] = []
        for e in self.furdok:
            if e.azonosito not in elso_alkalom and e.be_ki_lepett:
                if e.ki_ora >= 6 and e.ki_ora < 9:
                    elso_alkalom.append(e.azonosito)
                    hat_kilenc += 1
                    continue
                elif e.ki_ora >= 9 and e.ki_ora < 16:
                    elso_alkalom.append(e.azonosito)
                    kilenc_tizenhat += 1
                    continue
                elif e.ki_ora >= 16 and e.ki_ora < 20:
                    elso_alkalom.append(e.azonosito)
                    tizenhat_husz += 1
                    continue
        return [hat_kilenc, kilenc_tizenhat, tizenhat_husz]

    def __init__(self, forras: str):
        self.furdok = []
        with open(forras, 'r', encoding='utf-8')as file:
            for sor in file.read().splitlines():
                self.furdok.append(Furdo(sor))
