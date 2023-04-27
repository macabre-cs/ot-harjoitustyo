from tkinter import ttk, constants
import sys


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

        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        quit_label = ttk.Label(master=self._frame, text="Do you want to quit?")

        yes_button = ttk.Button(
            master=self._frame, text="YES", command=self._yes_clicked)
        no_button = ttk.Button(
            master=self._frame, text="NO", command=self._handle_back)

        quit_label.grid(row=0, column=0)
        yes_button.grid(row=1, column=0)
        no_button.grid(row=1, column=1)

    def _yes_clicked(self):
        sys.exit()
