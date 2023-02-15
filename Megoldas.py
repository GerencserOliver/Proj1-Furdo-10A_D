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

    def azonosito_lista(self, azonosito: int) -> int:
        azonosito_stat: dict[int, int] = {}
        for adat in self.furdok:
            if adat.azonosito not in azonosito_stat:
                azonosito_stat.setdefault(adat.azonosito, 0)
            else:
                azonosito_stat[adat.azonosito] += 1
        return azonosito_stat[azonosito]

    @property
    def legtobb_ido_eltoltve(self) -> list[int]:
        legtobb_ido_eltoltve: int = 0
        legtobb_idot_eltolto_ember: int = self.furdok[0].azonosito
        for i, adat in enumerate(self.furdok):
            count_skip = self.azonosito_lista(adat.azonosito)
            try:
                while adat.azonosito == self.furdok[i + 1].azonosito:
                    count_skip -= 1
                    if count_skip == 0:
                        break
                    i += 1
            except IndexError:
                if legtobb_ido_eltoltve < self.furdok[i].rekord_ideje_mp - adat.rekord_ideje_mp:
                    legtobb_idot_eltolto_ember = adat.azonosito
                    legtobb_ido_eltoltve = self.furdok[i].rekord_ideje_mp - adat.rekord_ideje_mp
                break
            if legtobb_ido_eltoltve < self.furdok[i + 1].rekord_ideje_mp - adat.rekord_ideje_mp:
                legtobb_idot_eltolto_ember = adat.azonosito
                legtobb_ido_eltoltve = self.furdok[i + 1].rekord_ideje_mp - adat.rekord_ideje_mp
        return [legtobb_idot_eltolto_ember, legtobb_ido_eltoltve]

    @property
    def adat_ido_kiiras(self) -> str:
        kiirni_valo = self.legtobb_ido_eltoltve
        return f'{kiirni_valo[0]}. vendég {kiirni_valo[1] // 3600}:{kiirni_valo[1] // 60 % 60}:{kiirni_valo[1] % 60}'

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
