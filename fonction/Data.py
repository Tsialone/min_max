from datetime import date
from display import Table
from objets.Box import Box
from form.Point import Point



class Data:

    table = None
    info = None
    fenetre = None
    players = None
    indexs_tour = [0 , 1]
    current_node = None
    terminal_node = []
    
    profondeur = 6
    point_noires = None
    nbr_gen6 = 0
    nbr_mandresy = 0
    
    moves = {
            Point(135, 135): [Point(135, 415), Point(415, 135), Point(415, 415)],
            Point(415, 135): [Point(135, 135), Point(695, 135), Point(415, 415)],
            Point(695, 135): [Point(695, 415), Point(415, 135), Point(415, 415)],

            Point(135, 415): [Point(135, 135), Point(135, 695), Point(415, 415)],
            Point(415, 415): [
                Point(135, 135), Point(415, 135), Point(695, 135),
                Point(135, 415), Point(695, 415),
                Point(135, 695), Point(415, 695), Point(695, 695)
            ],
            Point(695, 415): [Point(695, 135), Point(695, 695), Point(415, 415)],

            Point(135, 695): [Point(135, 415), Point(415, 415), Point(415, 695)],
            Point(415, 695): [Point(135, 695), Point(695, 695), Point(415, 415)],
            Point(695, 695): [Point(415, 695), Point(695, 415), Point(415, 415)],
        }

   

