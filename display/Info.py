import tkinter as tk
from tkinter import ttk
import display.Fenetre as F
from fonction.Ecouteur import Ecouteur

class Info(tk.Frame):
    def __init__(self, width: int, height: int, parent: F.Fenetre):
        super().__init__(parent, bg="lightgrey", width=width, height=height)
        self.pack_propagate(False)
        self.place(x=890, y=10)
        self.genererComponent()
        
    def genererComponent (self):
        btn_generer = tk.Button(self, text="Générer", command=Ecouteur.generer)
        btn_generer.place(x=10 , y=10)
        
       
        