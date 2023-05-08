from tkinter import ttk, constants, messagebox, IntVar, filedialog
from services.pet_service import pet_service, PetNameAlreadyInUseError
from ui.ui_style import apply_style
from PIL import ImageTk, Image
from pathlib import Path


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
        self._var = IntVar()

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
        self._create_pet_chooser()

        adopt_pet_button = ttk.Button(
            master=self._frame, text="Adopt a pet!", style="game.TButton", command=self._adopt_pet_handler)
        login_pet_button = ttk.Button(
            master=self._frame, text="I already have a pet", style="game.TButton", command=self._handle_show_login_view)

        adopt_pet_button.place(x=100, y=420)
        login_pet_button.place(x=300, y=420)

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

    def _create_pet_chooser(self):
        option1 = ttk.Radiobutton(master=self._frame, text="Option 1", variable=self._var,
                                  value=1, style="game.TRadiobutton", command=self._create_selected_pet)
        option2 = ttk.Radiobutton(master=self._frame, text="Option 2", variable=self._var,
                                  value=2, style="game.TRadiobutton", command=self._create_selected_pet)
        option3 = ttk.Radiobutton(master=self._frame, text="Option 3", variable=self._var,
                                  value=3, style="game.TRadiobutton", command=self._create_selected_pet)

        option1.place(x=40, y=250)
        option2.place(x=40, y=300)
        option3.place(x=40, y=350)

    def _create_selected_pet(self):
        self._create_selection_label()
        self._create_pet_image()

    def _create_pet_image(self):

        image_size = (160, 160)

        graphics_folder = Path(
            __file__).parent.parent.parent / "data"/"graphics"

        pet_image = Image.open(
            graphics_folder/pet_service.get_pet_img(self._var.get()))

        resized_image = pet_image.resize(image_size)

        photo = ImageTk.PhotoImage(resized_image)

        pet_img_label = ttk.Label(
            master=self._frame, style="bgcolor.TLabel", image=photo)

        pet_img_label.image = photo

        pet_img_label.place(x=450, y=240)

    def _create_selection_label(self):
        selection = f"You have selected \noption {self._var.get()}"
        selection_label = ttk.Label(
            master=self._frame, text=selection, style="gamev2.TLabel")
        selection_label.place(x=200, y=290)

    def _adopt_pet_handler(self):
        pet_name = self._pet_name_entry.get()
        password = self._password_entry.get()
        pet_img = pet_service.get_pet_img(self._var.get())

        if pet_name == "" or password == "" or pet_img == None:
            messagebox.showerror("Empty field error",
                                 "Name, secret word and pet are required")
            return

        try:
            pet_service.adopt_pet(pet_name, password, 0, pet_img)
            self._handle_adopt_pet()
        except PetNameAlreadyInUseError:
            messagebox.showerror("Pet already exists error",
                                 f"{pet_name} already exists!")
