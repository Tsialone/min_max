from shapely.geometry import Point
from form.Teboka import Teboka
from fonction.Fonction import Fonction
class Player:
    def __init__ (self , id_player:int , color:str):
        self.__id_player = id_player
        self.__teboka_grabed  = None
        self.__color = color
        self.__list_teboka = []
        
    def getColor (self):
        return self.__color
    def setColor (self , color:str):
        self.__color = color
        
    def getListTeboka  (self):
        return self.__list_teboka
    
    
    
    def getTebokaGrabed (self):
        return self.__teboka_grabed
    def setTebokaGrabed (self , teboka:Teboka):
        self.__teboka_grabed = teboka
    
    def getIdPlayer (self):
        return self.__id_player
    def setIdPlayer (self , id_player:int):
        self.setIdPLayer = id_player
        
    def addTeboka (self , teboka:Teboka):
        self.__list_teboka.append(teboka)
        
    def removeTeboka (self , teboka:Teboka):
        for tebo in self.__list_teboka:
            if tebo.getPoint() == teboka.getPoint():
                self.__list_teboka.remove(tebo)
                break
        
    def getTebokaPoints (self):
        points = []
        for teboka in self.__list_teboka:
            points.append(teboka.getPoint())
        return points
    
    def checkWin (self):
        teboka_point = self.getTebokaPoints()
        if  len (teboka_point) ==3:
            return Fonction.sont_colineaires(teboka_point)
        return False
        
        
   
    
    
        