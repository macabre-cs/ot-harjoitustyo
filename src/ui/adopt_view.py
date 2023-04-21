from tkinter import ttk, constants, messagebox
from services.pet_service import pet_service, PetNameAlreadyInUseError


class AdoptView:
    def __init__(self, root, handle_adopt_pet, handle_show_login_view):
        self._root = root
        self._handle_adopt_pet = handle_adopt_pet
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._pet_name_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._create_adopt_pet_field()
        self._create_password_field()

        adopt_pet_button = ttk.Button(
            master=self._frame, text="Adopt your new little friend!", command=self._adopt_pet_handler)
        login_pet_button = ttk.Button(
            master=self._frame, text="I already have a pet", command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        adopt_pet_button.grid(padx=5, pady=5)
        login_pet_button.grid(padx=5, pady=5)

    def _create_adopt_pet_field(self):
        pet_name_label = ttk.Label(
            master=self._frame, text="Name your new pet!")

        self._pet_name_entry = ttk.Entry(master=self._frame)

        pet_name_label.grid(padx=5, pady=5)
        self._pet_name_entry.grid(padx=5, pady=5)

    def _create_password_field(self):
        password_label = ttk.Label(
            master=self._frame, text="Secret word only you and your pet will know")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)

    def _adopt_pet_handler(self):
        pet_name = self._pet_name_entry.get()
        password = self._password_entry.get()

        if pet_name == "" or password == "":
            messagebox.showerror("Empty field error",
                                 "Name and secret word are required")
            return

        try:
            pet_service.adopt_pet(pet_name, password)
            self._handle_adopt_pet()
        except PetNameAlreadyInUseError:
            messagebox.showerror("Pet already exists error",
                                 f"{pet_name} already exists!")
