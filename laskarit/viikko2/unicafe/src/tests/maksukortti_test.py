import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_alkusaldo_ok(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(200)

        if self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa"):
            return True
        else:
            return False
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)

        if self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa"):
            return True
        
        else:
            return False