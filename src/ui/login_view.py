from tkinter import ttk, constants, messagebox
from services.pet_service import pet_service, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_login, handle_show_adopt_pet_view):
        self._root = root
        self._frame = None
        self._handle_login = handle_login
        self._handle_show_adopt_pet_view = handle_show_adopt_pet_view
        self._pet_name_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._create_pet_name_field()
        self._create_password_field()

        login_pet_button = ttk.Button(
            master=self._frame, text="Log in with your pet", command=self._login_handler)
        adopt_pet_button = ttk.Button(
            master=self._frame, text="Wait I don't have a pet yet", command=self._handle_show_adopt_pet_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        login_pet_button.grid(padx=5, pady=5)
        adopt_pet_button.grid(padx=5, pady=5)

    def _create_pet_name_field(self):
        pet_name_label = ttk.Label(master=self._frame, text="Pet name")

        self._pet_name_entry = ttk.Entry(master=self._frame)

        pet_name_label.grid(padx=5, pady=5)
        self._pet_name_entry.grid(padx=5, pady=5)

    def _create_password_field(self):
        password_label = ttk.Label(
            master=self._frame, text="Secret word")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)

    def _login_handler(self):
        pet_name = self._pet_name_entry.get()
        password = self._password_entry.get()

        try:
            pet_service.login_pet(pet_name, password)
            self._handle_login()
        except InvalidCredentialsError:
            messagebox.showerror(
                "Login failed", "Login failed, no such name or invalid secret word")
