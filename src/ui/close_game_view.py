from tkinter import ttk, constants
import sys
from ui.ui_style import apply_style


class CloseGameView:
    """Pelin lopetusnäkymä.
    """

    def __init__(self, root, handle_back):
        """CloseGameView-luokan konstruktori, jossa luodaan lopetusnäkymä.

        Args:
            root (TKinter-elementti): Juurikomponentti, johon näkymä alustetaan.
            handle_back (metodi): Kutsutaan kun käyttäjä ei haluakkaan lopettaa peliä.
        """
        self._root = root
        self._handle_back = handle_back
        self._frame = None

        apply_style()
        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(
            master=self._root, style="game.TFrame", width=640, height=500)
        quit_label = ttk.Label(
            master=self._frame, text="Do you want to quit?", style="game.TLabel")

        yes_button = ttk.Button(
            master=self._frame, text="YES", style="game.TButton", command=self._yes_clicked)
        no_button = ttk.Button(
            master=self._frame, text="NO", style="game.TButton", command=self._handle_back)

        quit_label.place(x=170, y=100)
        yes_button.place(x=170, y=370)
        no_button.place(x=350, y=370)

    def _yes_clicked(self):
        sys.exit()
