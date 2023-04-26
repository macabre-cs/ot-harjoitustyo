from tkinter import ttk, constants


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
        self._frame = ttk.Frame(
            master=self._root, borderwidth=5, relief="raised")
        welcome_label = ttk.Label(master=self._frame, text="Welcome back?")

        login_button = ttk.Button(
            master=self._frame, text="I already have a pet", command=self._handle_show_login_view, width=20)
        register_button = ttk.Button(
            master=self._frame, text="I don't have a pet yet", command=self._handle_show_adopt_view, width=20)

        welcome_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        login_button.grid(row=1, column=0, padx=10, pady=10)
        register_button.grid(row=1, column=1, padx=10, pady=10)
