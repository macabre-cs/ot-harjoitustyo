from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.geometry("640x500")
    window.resizable(False, False)
    window.title("Virtual pet")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
