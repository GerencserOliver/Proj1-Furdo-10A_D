from unittest import TestCase
from Megoldas import Megoldas


class test_Megoldas(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldas: Megoldas = Megoldas('furdoadat.txt')

    def test_elso_oltozo_kilepes(self):
        elso_kilepes = self.megoldas.elso_oltozo_kilepes
        utolso_kilepes = self.megoldas.utolso_oltozo_kilepes
        self.assertEqual(f'{elso_kilepes.ki_ora}:{elso_kilepes.ki_perc}:{elso_kilepes.ki_mp}', '6:14:56')
        self.assertEqual(f'{utolso_kilepes.ki_ora}:{utolso_kilepes.ki_perc}:{utolso_kilepes.ki_mp}', '18:35:37')

    def test_vendegek_reszlegen(self):
        self.assertEqual(self.megoldas.vendegek(), 33)

    def test_adat_ido_kiiras(self):
        self.assertEqual(self.megoldas.adat_ido_kiiras, '306. vendég 6:41:19')

    def test_vendegek_erkezes(self):
        self.assertEqual(self.megoldas.vendegek_erkezes[0], 9)
        self.assertEqual(self.megoldas.vendegek_erkezes[1], 45)
        self.assertEqual(self.megoldas.vendegek_erkezes[2], 46)

    def test_szauna_vendeg_idok(self):
        self.assertEqual(self.megoldas.adat_ido_kiiras, 'Fájlba kiírva.')

    def test_bent_voltak(self):
        self.assertEqual(len(self.megoldas.bent_voltak[0]), 41)
        self.assertEqual(len(self.megoldas.bent_voltak[1]), 52)
        self.assertEqual(len(self.megoldas.bent_voltak[2]), 54)
        self.assertEqual(len(self.megoldas.bent_voltak[3]), 48)
