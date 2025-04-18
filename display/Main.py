from fonction.Fonction import *
from display.Fenetre import *
from display.Table import *
from form.Node import Node
from form.Rectangle import *
import tkinter as tk
from fonction.Data import Data
from display.Info import Info
from objets.Player import Player

players = [Player(1, "red"), Player(2, "blue")]


# tena izy
fenetre = Fenetre("1500x880", "Fanorona telo")
table = Table(870, 850, fenetre, afficher=True)
info = Info(600, 850, fenetre)

Data.fenetre = fenetre
Data.info = info
Data.table = table
Data.players = players
Data.point_noires = [
    # Point(135 , 695)
    
]


for point_noire in Data.point_noires:
    Data.table.drawPoint(point_noire, "black")


fenetre.mainloop()




