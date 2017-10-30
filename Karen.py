import tkinter as tk
from tkinter import ttk
import webbrowser
import geminipy as Geminipy


def doorbell(event):
    print("doorbell rung")

def open_cp(event):
    webbrowser.open_new_tab("https://cleverprogrammer.com")

def open_amazon(event):
    webbrowser.open_new_tab("https://www.amazon.com/")

window = tk.Tk()
window.geometry("1920x1080")
label = ttk.Label(text="Welcome to Karen Cryptocurrency Trading Bot!", font="Verdana")
label.grid(column = 50, row  = 50)

button = ttk.Button(window, text="Doorbell")
button.grid(column = 0, row = 1)

button2 = ttk.Button(window, text="Clever Programmer")
button2.grid(column = 1, row = 1)

button3 = ttk.Button(window, text="Amazon")
button3.grid(column = 2, row = 1)

button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", open_cp)
button3.bind("<Button-1>", open_amazon)

window.mainloop()
