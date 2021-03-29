import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_luodussa_kassassa_oikea_rahamaara(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisten_lounaiden_myyntimaara_alussa_oikein(self):
        self.assertEqual(0, self.kassa.edulliset)

    def test_maukkaiden_lounaiden_myyntimaara_alussa_oikein(self):
        self.assertEqual(0, self.kassa.maukkaat)

    def test_syo_edullisesti_kateisella_antaa_oikean_vaihtorahan(self):
        maksu = 500
        self.assertEqual(500-240, self.kassa.syo_edullisesti_kateisella(maksu))

    def test_syo_edullisesti_kateisella_kasvattaa_vaihtokassaa_oikein(self):
        maksu = 500
        self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(100240, self.kassa.kassassa_rahaa)

    def test_myytyjen_edullisten_maara_kasvaa(self):
        maksu = 500
        self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(1, self.kassa.edulliset)

    def test_kassa_ei_kasva_jos_edullisesti_maksu_ei_riittava(self):
        maksu = 100
        self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(100000, self.kassa.kassassa_rahaa)

    def test_rahat_palautetaan_jos_edullisesti_maksu_ei_riittava(self):
        maksu = 100
        self.assertEqual(maksu, self.kassa.syo_edullisesti_kateisella(maksu))

    def test_myytyjen_maara_ei_kasva_jos_edullisesti_maksu_ei_riittava(self):
        maksu = 100
        self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(0, self.kassa.edulliset)
####
    def test_syo_maukkaasti_kateisella_antaa_oikean_vaihtorahan(self):
        maksu = 500
        self.assertEqual(500-400, self.kassa.syo_maukkaasti_kateisella(maksu))

    def test_syo_maukkaasti_kateisella_kasvattaa_vaihtokassaa_oikein(self):
        maksu = 500
        self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(100400, self.kassa.kassassa_rahaa)

    def test_myytyjen_maukkaasti_maara_kasvaa(self):
        maksu = 500
        self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(1, self.kassa.maukkaat)

    def test_kassa_ei_kasva_jos_maukkaasti_maksu_ei_riittava(self):
        maksu = 100
        self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(100000, self.kassa.kassassa_rahaa)

    def test_rahat_palautetaan_jos_maukkaasti_maksu_ei_riittava(self):
        maksu = 100
        self.assertEqual(maksu, self.kassa.syo_maukkaasti_kateisella(maksu))

    def test_myytyjen_maara_ei_kasva_jos_maukkaasti_maksu_ei_riittava(self):
        maksu = 100
        self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(0, self.kassa.edulliset)

### KORTTIOSTOT

#Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    def test_edullisesti_korttiostossa_veloitetaan_oikea_summa(self):
        maksukortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(1000-240, maksukortti.saldo)

    def test_maukkaasti_korttiostossa_veloitetaan_oikea_summa(self):
        maksukortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(1000-400, maksukortti.saldo)

    def test_edullisesti_korttiostossa_maksu_onnistuu(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(True, self.kassa.syo_edullisesti_kortilla(maksukortti))

    def test_maukkaasti_korttiostossa_maksu_onnistuu(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(True, self.kassa.syo_maukkaasti_kortilla(maksukortti))

#Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_syo_edullisesti_kortilla_kasvattaa_myynti_maaraa_jos_on_rahaa(self):
        maksukortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(1, self.kassa.edulliset)

    def test_syo_maukkaasti_kortilla_kasvattaa_myynti_maaraa_jos_on_rahaa(self):
        maksukortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(1, self.kassa.maukkaat)

#Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    def test_syo_edullisesti_kortilla_ei_veloita_jos_ei_rahaa(self):
        maksukortti = Maksukortti(10)
        self.kassa.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(10, maksukortti.saldo)

    def test_syo_maukkaasti_kortilla_ei_veloita_jos_ei_rahaa(self):
        maksukortti = Maksukortti(10)
        self.kassa.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(10, maksukortti.saldo)

    def test_syo_edullisesti_kortilla_ei_kasvata_myynti_maaraa_jos_ei_rahaa(self):
        maksukortti = Maksukortti(10)
        self.kassa.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(0, self.kassa.edulliset)

    def test_syo_maukkaasti_kortilla_ei_kasvata_myynti_maaraa_jos_ei_rahaa(self):
        maksukortti = Maksukortti(10)
        self.kassa.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(0, self.kassa.maukkaat)

    def test_edullisesti_korttiostossa_palauttaa_false_jos_kortilla_ei_rahaa(self):
        maksukortti = Maksukortti(10)
        self.assertEqual(False, self.kassa.syo_edullisesti_kortilla(maksukortti))

    def test_maukkaasti_korttiostossa_palauttaa_false_jos_kortilla_ei_rahaa(self):
        maksukortti = Maksukortti(10)
        self.assertEqual(False, self.kassa.syo_maukkaasti_kortilla(maksukortti))

#Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_syo_edullisesti_kortilla_ei_muuta_kassaa(self):
        maksukortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(100000, self.kassa.kassassa_rahaa)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassaa(self):
        maksukortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(100000, self.kassa.kassassa_rahaa)

#Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_lataa_rahaa_kortille_lataa_rahaa_kortille(self):
        maksukortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(1000, maksukortti.saldo)

    def test_lataa_rahaa_kortille_kasvattaa_kassaa(self):
        maksukortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(101000, self.kassa.kassassa_rahaa)

    def test_lataa_rahaa_ohittaa_negatiivisen_summan(self):
        maksukortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(0, maksukortti.saldo)






















