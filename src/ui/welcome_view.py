from tkinter import ttk, constants
from ui.ui_style import apply_style


class WelcomeView:
    """Sovelluksen aloitusnäkymä, jossa käyttäjä ohjataan kirjautumaan sisään tai adoptoimaan uuden lemmikin.
    """

    def __init__(self, root, handle_show_login_view, handle_show_adopt_view):
        """WelcomeView-luokan kontruktori, jossa luodaan aloitusnäkymä.

        Args:
            root (TKinter-elementti): Juurikomponentti, johon näkymä alustetaan.
            handle_show_login_view(metodi): Kutsuu kirjautumisnäkymän näyttävää metodia.
            handle_show_adopt_view (metodi): Kutsuu adoptointinäkymän näyttävää metodia.
        """
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_adopt_view = handle_show_adopt_view
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
        welcome_label = ttk.Label(
            master=self._frame, style="welcome.TLabel", text="Welcome back?")

        login_button = ttk.Button(
            master=self._frame, text="I already have a pet", style="game.TButton", command=self._handle_show_login_view)
        register_button = ttk.Button(
            master=self._frame, text="I don't have a pet yet", style="game.TButton", command=self._handle_show_adopt_view)

        welcome_label.place(relx=0.5, rely=0.3, anchor="center")
        login_button.place(relx=0.25, rely=0.7, anchor="center")
        register_button.place(relx=0.73, rely=0.7, anchor="center")
