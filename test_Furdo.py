from unittest import TestCase
from Furdo import Furdo


class test_Furdo(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sor1: Furdo = Furdo('112 0 1 6 14 56')
        cls.sor5: Furdo = Furdo('453 0 1 6 15 27')
        cls.sor14: Furdo = Furdo('399 0 0 7 9 33')
        cls.sor35: Furdo = Furdo('332 1 1 7 42 1')
        cls.sor53: Furdo = Furdo('217 0 1 9 10 9')

    def test_azonosito(self):
        self.assertEqual(self.sor1.furdozo_azonosito, 112)
        self.assertEqual(self.sor5.furdozo_azonosito, 453)
        self.assertEqual(self.sor14.furdozo_azonosito, 399)
        self.assertEqual(self.sor35.furdozo_azonosito, 332)
        self.assertEqual(self.sor53.furdozo_azonosito, 217)

    def test_furdo_azonosito(self):
        self.assertEqual(self.sor1.furdohelyseg_azonosito, 0)
        self.assertEqual(self.sor5.furdohelyseg_azonosito, 0)
        self.assertEqual(self.sor14.furdohelyseg_azonosito, 0)
        self.assertEqual(self.sor35.furdohelyseg_azonosito, 1)
        self.assertEqual(self.sor53.furdohelyseg_azonosito, 0)

    def test_be_ki_lepett(self):
        self.assertEqual(self.sor1.be_ki_lepett, False)
        self.assertEqual(self.sor5.be_ki_lepett, False)
        self.assertEqual(self.sor14.be_ki_lepett, True)
        self.assertEqual(self.sor35.be_ki_lepett, False)
        self.assertEqual(self.sor53.be_ki_lepett, False)

    def test_ki_ora(self):
        self.assertEqual(self.sor1.ki_ora, 6)
        self.assertEqual(self.sor5.ki_ora, 6)
        self.assertEqual(self.sor14.ki_ora, 7)
        self.assertEqual(self.sor35.ki_ora, 7)
        self.assertEqual(self.sor53.ki_ora, 9)

    def test_ki_perc(self):
        self.assertEqual(self.sor1.ki_perc, 14)
        self.assertEqual(self.sor5.ki_perc, 15)
        self.assertEqual(self.sor14.ki_perc, 9)
        self.assertEqual(self.sor35.ki_perc, 42)
        self.assertEqual(self.sor53.ki_perc, 10)

    def test_ki_mp(self):
        self.assertEqual(self.sor1.ki_mp, 56)
        self.assertEqual(self.sor5.ki_mp, 27)
        self.assertEqual(self.sor14.ki_mp, 33)
        self.assertEqual(self.sor35.ki_mp, 1)
        self.assertEqual(self.sor53.ki_mp, 9)
