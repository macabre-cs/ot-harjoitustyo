from tkinter import ttk, constants, messagebox
from PIL import ImageTk, Image
from pathlib import Path
import sys
import random
from services.pet_service import pet_service
from repositories.pet_repository import pet_repository


class MainView:
    def __init__(self, root, handle_close_game):
        self._root = root
        self._handle_close_game = handle_close_game
        self._frame = None
        self._pet = pet_service.get_current_pet()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        name_label = ttk.Label(master=self._frame, text=f"{self._pet.name}")
        button1 = ttk.Button(master=self._frame, text="Love",
                             command=self._love_clicked)
        button2 = ttk.Button(master=self._frame, text="Feed",
                             command=self._feed_clicked)
        button3 = ttk.Button(
            master=self._frame, text="Hurt :(", command=self._hurt_clicked)

        button4 = ttk.Button(
            master=self._frame, text="Close game", command=self._handle_close_game)

        graphics_folder = Path(
            __file__).parent.parent.parent / "data"/"graphics"

        pet_image = Image.open(graphics_folder/"Rotta_Otus_300x300.png")

        photo = ImageTk.PhotoImage(pet_image)

        pet_img_label = ttk.Label(master=self._frame, image=photo)
        pet_img_label.image = photo

        name_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        pet_img_label.grid(row=1, column=0, columnspan=3)

        button1.grid(row=2, column=0, padx=10, pady=10)
        button2.grid(row=2, column=1, padx=10, pady=10)
        button3.grid(row=2, column=2, padx=10, pady=10)
        button4.grid(row=3, column=0, padx=10, pady=10)

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
