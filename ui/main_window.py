# used for the main window
import tkinter as tk
# used for welcome labels
from ui.labels import H1Label, H6Label


class MainWindow:
    # root window properties
    def __init__(self):
        self.root = tk.Tk()
        #  
        self.bg = "#222222"
        self.root.configure(background = self.bg)
        width, height = 400, 600
        # get height and width of screen
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth()
        # determine center placement for window
        x = (window_width // 2) - (width // 2)
        y = (window_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Quick DB")
        
        welcome = H1Label(self.root, text = "Welcome")
        welcome.pack(pady = (45, 0))
        
        choose_file = H6Label(self.root, text = "Choose a file")
        choose_file.pack(pady = (0, 0))
    # start the root window
    def run(self):
        self.root.mainloop()