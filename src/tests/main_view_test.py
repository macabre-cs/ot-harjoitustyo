import unittest
from tkinter import Tk

from ui.main_view import MainView

class TestMainView(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.view = MainView(self.root, None)
    
    def tearDown(self):
        self.view.destroy()
        self.root.destroy()
    
    def test_destroy(self):
        self.view.destroy()
        self.assertFalse(self.view._frame.winfo_exists())

    def test_love_clicked_works(self):  #testataan toimiiko metodit
        self.view._love_clicked()
        
    
    def test_feed_clicked_works(self):
        self.view._feed_clicked()
        
    def test_hurt_clicked_works(self):
        with self.assertRaises(SystemExit):
            self.view._hurt_clicked()
            

if __name__=="__main__":
    unittest.main()
