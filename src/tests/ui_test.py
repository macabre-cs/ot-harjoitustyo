import unittest
from unittest.mock import MagicMock, patch

from ui.ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.root = MagicMock()
    
    def test_start_works(self):  #testataan toimiiko UI-luokan käynnistys oikein
        ui = UI(self.root)

        with patch.object(ui, "_show_main_view") as mock_show_main_view:
            ui.start()
            mock_show_main_view.assert_called_once()

    def test_handle_close_game_works(self): 
        ui = UI(self.root)

        with patch.object(ui, "_show_close_game_view") as mock_show_close_game_view:
            ui._handle_close_game()
            mock_show_close_game_view.assert_called_once()

    def test_handle_back_works(self):
        ui = UI(self.root)

        with patch.object(ui, "_show_main_view") as mock_show_main_view:
            ui._handle_back()
            mock_show_main_view.assert_called_once()
    


if __name__=="__main__":
    unittest.main()