from fonction.Fonction import *
from display.Fenetre import *
from display.Table import *
from form.Rectangle import *
import tkinter as tk
from fonction.Data import Data
from display.Info import Info
from objets.Player import Player

players = [
    Player (1 , "red") , 
    Player(2 , "blue")
]


fenetre = Fenetre("1500x880" ,"Fanorona telo")
table  = Table(870 , 850 , fenetre)
info = Info(600 , 850 , fenetre)

Data.fenetre = fenetre
Data.info  =info
Data.table = table
Data.players = players


# Data.drawMarcher(carte)
# Data.drawTextMarcher()
fenetre.mainloop()




    




