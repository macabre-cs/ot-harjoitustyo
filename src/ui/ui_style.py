import tkinter as tk
from tkinter import ttk


def apply_style():
    s = ttk.Style()
    s.configure("game.TFrame", background="#fff0f5",
                borderwidth=12, relief="raised")
    s.configure("game.TButton", font="Terminal",
                background="#ccf0f8", borderwidth=3, relief="raised")
    s.configure("game.TLabel", font=("Terminal", 16), background="#fff0f5")
    s.configure("gamev2.TLabel", font=("Terminal", 13), background="#fff0f5")
    s.configure("game.TEntry", font=("Terminal", 10),
                backround="#f0f8ff", relief="raised")
    s.configure("bgcolor.TLabel", background="#fff0f5")
    s.configure("name.TLabel", font=("Terminal", 16), background="#ccf0f8",
                borderwidth=3, relief="raised", anchor="center")
