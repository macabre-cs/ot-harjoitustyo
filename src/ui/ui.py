from ui.main_view import MainView
from ui.close_game_view import CloseGameView
from ui.welcome_view import WelcomeView
from ui.adopt_view import AdoptView
from ui.login_view import LoginView


class UI:
    """Luokka, joka vastaa sovelluksen käyttöliittymästä
    """
    def __init__(self, root):
        """UI-luokan kontruktori jossa luodaan luokka, joka vastaa käyttöliittymästä.

        Args:
            root (TKinter-elementti): Käyttöliittymän juurikomponentti, jonka sisään käyttöliittymä alustetaan.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän näyttämällä aloitusnäkymän.
        """
        self._show_welcome_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_close_game(self):
        self._show_close_game_view()

    def _handle_back(self):
        self._show_main_view()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(self._root, self._handle_close_game)

        self._current_view.pack()

    def _show_close_game_view(self):
        self._hide_current_view()

        self._current_view = CloseGameView(self._root, self._handle_back)

        self._current_view.pack()

    def _show_welcome_view(self):
        self._hide_current_view()

        self._current_view = WelcomeView(
            self._root, self._show_login_view, self._show_adopt_pet_view)

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_main_view, self._show_adopt_pet_view)

        self._current_view.pack()

    def _show_adopt_pet_view(self):
        self._hide_current_view()

        self._current_view = AdoptView(
            self._root, self._show_main_view, self._show_login_view)

        self._current_view.pack()
