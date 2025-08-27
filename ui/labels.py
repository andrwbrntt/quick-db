import tkinter as tk

# custom label classes
class H1Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        # get the parent bg color
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 32, "bold"),
            bg = bg,
            **kwargs
            )

class H6Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 12),
            bg = bg,
            **kwargs
            )