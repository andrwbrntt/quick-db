# used for the main window
import tkinter as tk
# used for welcome labels
from ui.labels import H1Label, H6Label
from ui.buttons import LargeButton
# used to handle button functions
from ui.handlers import handle_csv, handle_excel, handle_db


class MainWindow:
    # root window properties
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(background = "#222222")
        width, height = 300, 450
        # get height and width of screen
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth()
        # determine center placement for window
        x = (window_width // 2) - (width // 2)
        y = (window_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Quick DB")
        
        # main window labels
        welcome_label = H1Label(self.root, text = "Welcome")
        welcome_label.pack(pady = (45, 0))
        
        choose_file_label = H6Label(self.root, text = "Choose a file")
        choose_file_label.pack(pady = (0, 0))
        
        # main window buttons
        csv_button = LargeButton(self.root, text = ".csv", command = handle_csv)
        csv_button.pack(pady = (45,0))
        
        excel_button = LargeButton(self.root, text = ".xlsx", command = handle_excel)
        excel_button.pack(pady = (25, 0))
        
        db_button = LargeButton(self.root, text = ".db", command = handle_db)
        db_button.pack(pady = (25, 0))

    # start the root window
    def run(self):
        self.root.mainloop()