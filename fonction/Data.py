from datetime import date
from display import Table
from objets.Box import Box
from shapely.geometry import Point



class Data:

    table = None
    info = None
    fenetre = None
    players = None
    indexs_tour = [0 , 1]
    current_node = None
    terminal_node = []
    
    profondeur = 5
    point_noires = None
    nbr_gen6 = 0
    nbr_mandresy = 0


