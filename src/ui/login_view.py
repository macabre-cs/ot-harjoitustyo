from tkinter import ttk, constants, messagebox
from services.pet_service import pet_service, InvalidCredentialsError
from ui.ui_style import apply_style


class LoginView:
    """Sovelluksen kirjautumisnäkymä, jossa käyttäjä voi kirjautua sisään.
    """

    def __init__(self, root, handle_login, handle_show_adopt_pet_view):
        """LoginView-luokan konstruktori, jossa luodaan kirjautumisnäkymä.

        Args:
            root (TKinter-elementti): Juurikomponentti, johon näkymä alustetaan.
            handle_login (metodi): Kutsutaan käyttäjän kirjautuessa sisään.
            handle_show_adopt_pet_view (metodi): Kutsuu adoptointinäkymän näyttävää metodia.
        """
        self._root = root
        self._frame = None
        self._handle_login = handle_login
        self._handle_show_adopt_pet_view = handle_show_adopt_pet_view
        self._pet_name_entry = None
        self._password_entry = None

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

        self._create_pet_name_field()
        self._create_password_field()

        login_pet_button = ttk.Button(
            master=self._frame, text="Log in with your pet", style="game.TButton", command=self._login_handler)
        adopt_pet_button = ttk.Button(
            master=self._frame, text="Wait I don't have a pet yet", style="game.TButton", command=self._handle_show_adopt_pet_view)

        login_pet_button.place(x=190, y=320)
        adopt_pet_button.place(x=150, y=400)

    def _create_pet_name_field(self):
        pet_name_label = ttk.Label(
            master=self._frame, text="Pet name", style="gamev2.TLabel")

        self._pet_name_entry = ttk.Entry(
            master=self._frame, style="game.TEntry")

        pet_name_label.place(x=260, y=50)
        self._pet_name_entry.place(x=200, y=100, width=250, height=30)

    def _create_password_field(self):
        password_label = ttk.Label(
            master=self._frame, text="Secret word", style="gamev2.TLabel")

        self._password_entry = ttk.Entry(
            master=self._frame, style="game.TEntry")

        password_label.place(x=250, y=150)
        self._password_entry.place(x=200, y=200, width=250, height=30)

    def _login_handler(self):
        pet_name = self._pet_name_entry.get()
        password = self._password_entry.get()

        try:
            pet_service.login_pet(pet_name, password)
            self._handle_login()
        except InvalidCredentialsError:
            messagebox.showerror(
                "Login failed", "Login failed, no such name or invalid secret word")
