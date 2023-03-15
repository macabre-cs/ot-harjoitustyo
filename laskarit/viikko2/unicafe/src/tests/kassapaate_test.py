import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    # apumetodi muille testeille, sain apua discordista
    def assert_kassapaate(self, rahaa, edulliset, maukkaat):
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertEqual(self.kassapaate.edulliset, edulliset)
        self.assertEqual(self.kassapaate.maukkaat, maukkaat)

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_rahamaara_ja_myynti_ok(self):
        self.assert_kassapaate(100000, 0, 0)
    
    def test_edullinen_kateisosto_ok(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)
        self.assert_kassapaate(100240, 1, 0)
    
    def test_maukas_kateisosto_ok(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)
        self.assert_kassapaate(100400, 0, 1)
    
    def test_edullinen_kateisosto_ei_rahaa_ok(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assert_kassapaate(100000, 0, 0)

    def test_maukas_kateisosto_ei_rahaa_ok(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assert_kassapaate(100000, 0, 0)
    
    def test_edullinen_korttiosto_ok(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assert_kassapaate(100000, 1, 0)
        if vastaus == True and self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa"):
            return True
        else:
            return False
        
    def test_maukas_korttiosto_ok(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assert_kassapaate(100000, 0, 1)
        if vastaus == True and self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa"):
            return True
        else:
            return False
    
    def test_edullinen_korttiosto_ei_rahaa_ok(self):
        maksukortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assert_kassapaate(100000, 0, 0)
        if vastaus == False and self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa"):
            return False

    def test_maukas_korttiosto_ei_rahaa_ok(self):
        maksukortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assert_kassapaate(100000, 0, 0)
        if vastaus == False and self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa"):
            return False
    
    def test_kortin_lataus_ok(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 30.00 euroa")
        self.assert_kassapaate(102000, 0, 0)
    
    def test_kortin_lataus_ei_ok_neg_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assert_kassapaate(100000, 0, 0)