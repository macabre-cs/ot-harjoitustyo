from tkinter import ttk, constants, messagebox
from services.pet_service import pet_service, PetNameAlreadyInUseError
from ui.ui_style import apply_style


class AdoptView:
    """Virtuaalilemmikin adoptointinäkymä, jossa käyttäjä voi ''rekisteröityä''.
    """

    def __init__(self, root, handle_adopt_pet, handle_show_login_view):
        """AdoptView-luokan konstruktori, jossa luodaan adoptointinäkymä.

        Args:
            root (TKinter-elementti): Juurikomponentti, johon näkymä alustetaan.
            handle_adopt_pet (metodi): Kutsutaan käyttäjän adoptoidessa virtuaalilemmikin.
            handle_show_login_view (metodi): Kutsuu kirjautumisnäkymän näyttävää metodia.
        """
        self._root = root
        self._handle_adopt_pet = handle_adopt_pet
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
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

        self._create_adopt_pet_field()
        self._create_password_field()

        adopt_pet_button = ttk.Button(
            master=self._frame, text="Adopt your new little friend!", style="game.TButton", command=self._adopt_pet_handler)
        login_pet_button = ttk.Button(
            master=self._frame, text="I already have a pet", style="game.TButton", command=self._handle_show_login_view)

        adopt_pet_button.place(x=140, y=320)
        login_pet_button.place(x=190, y=400)

    def _create_adopt_pet_field(self):
        pet_name_label = ttk.Label(
            master=self._frame, text="Name your new pet!", style="gamev2.TLabel")

        self._pet_name_entry = ttk.Entry(
            master=self._frame, style="game.TEntry")

        pet_name_label.place(x=200, y=50)
        self._pet_name_entry.place(x=200, y=100, width=250, height=30)

    def _create_password_field(self):
        password_label = ttk.Label(
            master=self._frame, text="Secret word only you and your pet will know", style="gamev2.TLabel")

        self._password_entry = ttk.Entry(
            master=self._frame, style="game.TEntry")

        password_label.place(x=40, y=150)
        self._password_entry.place(x=200, y=200, width=250, height=30)

    def _adopt_pet_handler(self):
        pet_name = self._pet_name_entry.get()
        password = self._password_entry.get()

        if pet_name == "" or password == "":
            messagebox.showerror("Empty field error",
                                 "Name and secret word are required")
            return

        try:
            pet_service.adopt_pet(pet_name, password, 0)
            self._handle_adopt_pet()
        except PetNameAlreadyInUseError:
            messagebox.showerror("Pet already exists error",
                                 f"{pet_name} already exists!")
