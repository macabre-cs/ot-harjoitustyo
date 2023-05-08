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
        self._progress_bar = None

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

        self._create_progress_bar()
        self._create_buttons()
        self._create_image()
        self._create_name_label()

    def _love_clicked(self):
        love_choices = ["You gave your virtual pet some headpats!",
                        "You gave your virtual pet some love!",
                        "You gave your virtual pet a hug!",
                        "You gave your virtual pet your credit card information!"]
        messagebox.showinfo(message=random.choice(love_choices))
        self._progress(20)

    def _feed_clicked(self):
        food_choices = ["You gave your virtual pet some spaghetti!",
                        "You gave your virtual pet some rat food!",
                        "You gave your virtual pet some potato chips!",
                        "You gave your virtual pet some leftovers!"]
        messagebox.showinfo(message=random.choice(food_choices))
        self._progress(10)

    def _hurt_clicked(self):
        hurt_choices = [":(",
                        "You don't deserve your virtual pet anymore.",
                        "Bad!!!",
                        "ei kyl ollu fresh"]
        messagebox.showinfo(message=random.choice(hurt_choices))
        pet_repository.punish_player(self._pet.name)
        pet_repository.cleanup_data()
        sys.exit()

    def _create_name_label(self):
        name_label = ttk.Label(
            master=self._frame, text=f"{self._pet.name}", style="name.TLabel")

        extra_width = 0

        if len(self._pet.name) > 13:
            extra_width = (len(self._pet.name)-13)*18

        name_label.place(relx=0.5, rely=0.1, width=240 +
                         extra_width, height=40, anchor="center")

    def _create_image(self):
        graphics_folder = Path(
            __file__).parent.parent.parent / "data"/"graphics"

        pet_image = Image.open(graphics_folder/self._pet.image)

        photo = ImageTk.PhotoImage(pet_image)

        pet_img_label = ttk.Label(
            master=self._frame, style="bgcolor.TLabel", image=photo)

        pet_img_label.image = photo

        pet_img_label.place(x=170, y=90)

    def _create_buttons(self):
        button1 = ttk.Button(master=self._frame, text="Love", style="game.TButton",
                             command=self._love_clicked)
        button2 = ttk.Button(master=self._frame, text="Feed", style="game.TButton",
                             command=self._feed_clicked)
        button3 = ttk.Button(
            master=self._frame, text="Hurt :(", style="game.TButton", command=self._hurt_clicked)

        button4 = ttk.Button(
            master=self._frame, text="Close game", style="game.TButton", command=self._handle_close_game)

        button1.place(x=50, y=420)
        button2.place(x=190, y=420)
        button3.place(x=330, y=420)
        button4.place(x=470, y=420)

    def _create_progress_bar(self):
        self._progress_bar = ttk.Progressbar(
            master=self._frame, style="game.Vertical.TProgressbar", orient="vertical", length=300, mode="determinate")
        self._progress_bar["value"] = pet_service.get_progress()
        self._progress_bar.place(x=30, y=80)

    def _progress(self, progress: int):
        if self._progress_bar["value"] < 100:
            self._progress_bar["value"] += progress
            pet_service.save_progress(
                self._progress_bar["value"], self._pet.name)
        if self._progress_bar["value"] >= 100:
            messagebox.showinfo(message="Your virtual pet loves you!")
            pet_service.save_progress(
                self._progress_bar["value"], self._pet.name)
