from tkinter import filedialog
from tkinter import messagebox

def handle_csv():
    file_path = filedialog.askopenfilename(
        filetypes = [(".csv files", "*.csv")],
        title = "Select .csv"
    )

def handle_excel():
    file_path = filedialog.askopenfilename(
        filetypes=[(".xlsx files", "*.xlsx")],
        title = "Select .xlsx file"
    )
    
def handle_db():
    file_path = filedialog.askopenfilename(
        filetypes = [(".db files", "*.db")],
        title = ".db files"
    )