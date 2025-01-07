import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "HOLAAAA")

root = tk.Tk()
root.title("SALUDO")  # Set the window title
root.geometry("400x400")  # Resize the root window to 400x400 pixels
root.deiconify()  # Make the root window visible

button = tk.Button(root, text="Show Message", command=show_message)
button.pack(pady=20)

root.mainloop()
