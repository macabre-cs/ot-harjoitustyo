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

    def test_destroy_works(self):
        self.view.destroy()
        self.assertFalse(self.view._frame.winfo_exists())


if __name__ == "__main__":
    unittest.main()
