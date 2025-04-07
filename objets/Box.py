from datetime import *
from form.Rectangle import Rectangle
from form.Teboka import Teboka
from shapely.geometry import Point




class Box(Rectangle):
    def __init__(self,  x , y , idBox , longeur, largeur):
        super().__init__(x, y, largeur, longeur)
        self.__idBox = idBox
        self.__longeur = longeur 
        self.__largeur = largeur 
       
        
    def getIdBox(self):
        return self.__idBox
    def getLongueur(self):
        return self.__longeur


    def getLargeur(self):
        return self.__largeur
    
    


