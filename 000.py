import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "HOLAAAA")

root = tk.Tk()
root.withdraw()  # Hide the root window
show_message()
root.mainloop()
