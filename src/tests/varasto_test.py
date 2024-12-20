import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    # OMATEKEMÄ
    def test_ottaa_liikaa(self):
        self.varasto.ota_varastosta(11)
    #

    # OMATEKEMÄ
    def test_laittaa_varastoon(self):
        self.varasto.lisaa_varastoon(8)
    #

    # OMATEKEMÄ
    def test_lisataan_pienempinolla(self):
        self.varasto.lisaa_varastoon(-2)
    #

     # OMATEKEMÄ
    def test_laittaa_liikaa_varastoon(self):
        self.varasto.lisaa_varastoon(13)
    #

    # OMATEKEMÄ
    def test_ottaa_vahemmankun_nolla(self):
        self.varasto.ota_varastosta(-2)
    #

    # OMATEKEMÄ
    def test_konstruktori_tilavuus_negatiivinen(self):
        varasto_negatiivinen = Varasto(-5)
        self.assertAlmostEqual(varasto_negatiivinen.tilavuus, 0.0)
    #

    # OMATEKEMÄ
    def test_konstruktori_alku_saldo_negatiivinen(self):
        varasto_saldo_negatiivinen = Varasto(10, -5)
        self.assertAlmostEqual(varasto_saldo_negatiivinen.saldo, 0.0)
    #

    # OMATEKEMÄ
    def test_returnaa_tilatiedot(self):
        self.varastontilanne = Varasto(10, 5)
        self.assertEqual(str(self.varastontilanne), "saldo = 5, vielä tilaa 5")
    #

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
