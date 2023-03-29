import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, ttk
from PIL import ImageTk, Image
from user_interface import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.ui = UI(self.root)
    
    def tearDown(self):
        self.root.destroy()

    @patch('builtins.print')
    def test_love_clicked_works(self, mock_print):
        self.ui._love_clicked()
        mock_print.assert_called_once_with("You gave your virtual pet some headpats!")

    @patch('builtins.print')
    def test_feed_clicked_works(self, mock_print):
        self.ui._feed_clicked()
        mock_print.assert_called_once_with("You fed your virtual pet some spaghetti!")

    @patch('builtins.print')
    def test_hurt_clicked_works(self, mock_print):
        with patch.object(UI, '_close_window') as mock_close:
            self.ui._hurt_clicked()
            mock_print.assert_called_once_with("You don't deserve your virtual pet anymore.")
            mock_close.assert_called_once()

    def test_close_window_works(self):
        with patch.object(Tk, 'destroy') as mock_destroy:
            self.ui._close_window()
            mock_destroy.assert_called_once()
