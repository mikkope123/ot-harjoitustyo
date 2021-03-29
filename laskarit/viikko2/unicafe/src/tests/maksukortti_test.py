import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldon_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_otto_palauttaa_true_onnistuessaan(self):
        self.maksukortti.lataa_rahaa(100)
        palautusarvo = self.maksukortti.ota_rahaa(100)
        self.assertEqual(True, palautusarvo)

    def test_rahan_otto_palauttaa_fakse_epaonnistuessaan(self):
        palautusarvo = self.maksukortti.ota_rahaa(100)
        self.assertEqual(False, palautusarvo)
