from tkinter import Tk, ttk
from PIL import ImageTk, Image

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        name_label = ttk.Label(master=self._root, text="Pet name")
        button1 = ttk.Button(master=self._root, text="Love", command=self._love_clicked)
        button2 = ttk.Button(master=self._root, text="Feed", command=self._feed_clicked)
        button3 = ttk.Button(master=self._root, text="Hurt :(", command=self._hurt_clicked)
        
        pet_image = Image.open("dokumentaatio/kuvat/Rotta_Otus_300x300.png")
        photo = ImageTk.PhotoImage(pet_image)

        pet_img_label = ttk.Label(master=self._root, image=photo)
        pet_img_label.image = photo

        name_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        pet_img_label.grid(row=1, column=0, columnspan=3)

        button1.grid(row=2, column=0, padx=10, pady=10)
        button2.grid(row=2, column=1, padx=10, pady=10)
        button3.grid(row=2, column=2, padx=10, pady=10)
    
    def _love_clicked(self):
        print(f"You gave your virtual pet some headpats!")

    def _feed_clicked(self):
        print(f"You fed your virtual pet some spaghetti!")
    
    def _hurt_clicked(self):
        print(f"You don't deserve your virtual pet anymore.")
        self._close_window()
    
    def _close_window(self):
        window.destroy()

window = Tk()
window.title("Virtual pet")

ui = UI(window)
ui.start()

window.mainloop()