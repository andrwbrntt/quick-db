import tkinter as tk

class LargeButton(tk.Button):
    def __init__(self, parent, text = "", **kwargs):
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 24, "bold"),
            fg = "#222222",
            anchor = "center",
            width = 10,
            height = 1,
            relief = "flat",
            borderwidth = 0,
            **kwargs
            )