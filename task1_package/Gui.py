import tkinter as tk
from tkinter import Button, Tk

class Gui():
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.geometry('350*200')
        self.root.mainloop()
       

g=Gui()