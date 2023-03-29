from tkinter import ttk, constants

class NamePetView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._start_game()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _start_game(self):
        self._frame = ttk.Frame(master=self._root)
        test_label = ttk.Label(master=self._frame, text="Test")

        test_label.grid(row=0, column=0)
