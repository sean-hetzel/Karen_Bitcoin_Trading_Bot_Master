import tkinter as tk
from geminipy import Geminipy

LARGE_FONT = ("Verdana", 12)

class gemini_btc(tk.Tk):
    def __itit__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne):
            frame = StartPage(container, self)
            self.frames[StartPage] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="start page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(slef, text="Visit page 1",
                            command=lambda: conotroller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        fk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(slef, text="Back to Home",
                            command=lambda: conotroller.show_frame(StartPage))
        button1.pack()
        
app = gemini_btc()
app.mainloop()
