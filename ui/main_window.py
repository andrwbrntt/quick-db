# used for the main window
import tkinter as tk

class MainWindow:
    # root window properties
    def __init__(self):
        self.root = tk.Tk()
        height, width = 1100, 800
        # get height and width of screen
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth()
        # determine center placement for window
        x = (window_width // 2) - (width // 2)
        y = (window_height // 2) - (height // 2)
        self.root.geometry(f"{height}x{width}+{x}+{y}")
        self.root.title("Quick DB")
    # start the root window
    def run(self):
        self.root.mainloop()