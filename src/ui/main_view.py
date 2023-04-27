from tkinter import ttk, constants, messagebox
from PIL import ImageTk, Image
from pathlib import Path
import sys
import random
from services.pet_service import pet_service
from repositories.pet_repository import pet_repository
from ui.ui_style import apply_style


class MainView:
    """Sovelluksen päänäkymä.
    """

    def __init__(self, root, handle_close_game):
        """MainView-luokan konstruktori, jossa luodaan päänäkymä.

        Args:
            root (TKinter-elementti): Juurikomponentti, johon näkymä alustetaan.
            handle_close_game (metodi): Kutsutaan kun käyttäjä lopettaa pelin.
        """
        self._root = root
        self._handle_close_game = handle_close_game
        self._frame = None
        self._pet = pet_service.get_current_pet()

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
        name_label = ttk.Label(
            master=self._frame, text=f"{self._pet.name}", style="name.TLabel")
        button1 = ttk.Button(master=self._frame, text="Love", style="game.TButton",
                             command=self._love_clicked)
        button2 = ttk.Button(master=self._frame, text="Feed", style="game.TButton",
                             command=self._feed_clicked)
        button3 = ttk.Button(
            master=self._frame, text="Hurt :(", style="game.TButton", command=self._hurt_clicked)

        button4 = ttk.Button(
            master=self._frame, text="Close game", style="game.TButton", command=self._handle_close_game)

        graphics_folder = Path(
            __file__).parent.parent.parent / "data"/"graphics"

        pet_image = Image.open(graphics_folder/"Rotta_Otus_300x300.png")

        photo = ImageTk.PhotoImage(pet_image)

        pet_img_label = ttk.Label(
            master=self._frame, style="bgcolor.TLabel", image=photo)
        pet_img_label.image = photo

        name_label.place(x=200, y=30, width=240, height=40)
        pet_img_label.place(x=170, y=90)
        button1.place(x=50, y=420)
        button2.place(x=190, y=420)
        button3.place(x=330, y=420)
        button4.place(x=470, y=420)

    def _love_clicked(self):
        love_choices = ["You gave your virtual pet some headpats!",
                        "You gave your virtual pet some love!",
                        "You gave your virtual pet a hug!",
                        "You gave your virtual pet your credit card information!"]
        messagebox.showinfo(message=random.choice(love_choices))

    def _feed_clicked(self):
        food_choices = ["You gave your virtual pet some spaghetti!",
                        "You gave your virtual pet some rat food!",
                        "You gave your virtual pet some potato chips!",
                        "You gave your virtual pet some leftovers!"]
        messagebox.showinfo(message=random.choice(food_choices))

    def _hurt_clicked(self):
        hurt_choices = [":(",
                        "You don't deserve your virtual pet anymore.",
                        "Bad!!!",
                        "ei kyl ollu fresh"]
        messagebox.showinfo(message=random.choice(hurt_choices))
        pet_repository.punish_player(self._pet.name)
        pet_repository.cleanup_data()
        sys.exit()
