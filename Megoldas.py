from Furdo import Furdo


class Megoldas:
    furdok: list[Furdo]

    def __init__(self, forras: str):
        self.furdok = []
        with open(forras, 'r', encoding='utf-8')as file:
            for sor in file.read().splitlines():
                self.furdok.append(Furdo(sor))
