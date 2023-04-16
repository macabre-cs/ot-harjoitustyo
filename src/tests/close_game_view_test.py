import unittest
from unittest.mock import Mock
from tkinter import Tk
from ui.close_game_view import CloseGameView


class TestCloseGameView(unittest.TestCase):

    def setUp(self):
        self.root = Tk()

    def tearDown(self):
        self.root.destroy()

    def test_yes_clicked_works(self):
        view = CloseGameView(self.root, Mock())
        with self.assertRaises(SystemExit):
            view._yes_clicked()