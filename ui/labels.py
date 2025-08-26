import tkinter as tk

class H1Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 32, "bold"),
            fg = "#FFFBFE",
            bg = bg,
            **kwargs
            )

class H2Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 24, "bold"),
            fg = "#FFFBFE",
            bg = bg,
            **kwargs
            )

class H3Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 18, "bold"),
            fg = "#FFFBFE",
            bg = bg,
            **kwargs
            )

class H4Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 16, "bold"),
            fg = "#FFFBFE",
            bg = bg,
            **kwargs
            )

class H5Label(tk.Label):
    def __init__(self, parent, text = "", **kwargs):
        bg = kwargs.pop("bg", parent["bg"])
        super().__init__(
            parent,
            text = text,
            font = ("Helvetica", 14, "bold"),
            fg = "#FFFBFE",
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
            fg = "#FF5A5F",
            bg = bg,
            **kwargs
            )