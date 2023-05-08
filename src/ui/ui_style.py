import tkinter as tk
from tkinter import ttk


def apply_style():
    """Sovelluksen graafisen käyttöliittymän tyylistä vastaava funktio.
    """
    s = ttk.Style()
    s.configure("game.TFrame", background="#fff0f5",
                borderwidth=12, relief="raised")
    s.configure("game.TButton", font="Terminal",
                background="#ccf0f8", borderwidth=3, relief="raised")
    s.configure("game.TLabel", font=("Terminal", 16), background="#fff0f5")
    s.configure("gamev2.TLabel", font=("Terminal", 13),
                background="#fff0f5", justify="center")
    s.configure("game.TEntry", font=("Terminal", 10),
                backround="#f0f8ff", relief="raised")
    s.configure("bgcolor.TLabel", background="#fff0f5")
    s.configure("name.TLabel", font=("Terminal", 16), background="#ccf0f8",
                borderwidth=3, relief="raised", anchor="center")
    s.configure("game.Vertical.TProgressbar", throughcolor="#add8e6",
                background="#fddde6", bordercolor="#add8e6", borderwidth=3)
    s.configure("game.TRadiobutton", background="#ccf0f8", font=("Terminal", 12), indicatorcolor="#fddde6",
                relief="raised", indicatorbackground="#fddde6", indicatorrelief="raised", highlightcolor="#f0f8ff", fg="#fddde6")
