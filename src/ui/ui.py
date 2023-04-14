from ui.main_view import MainView
from ui.close_game_view import CloseGameView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_view()

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
