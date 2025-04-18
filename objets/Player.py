from form.Point import Point
from form.Teboka import Teboka
from fonction.Fonction import Fonction
class Player:
    def __init__ (self , id_player:int , color:str):
        self.__id_player = id_player
        self.__score = None
        self.__teboka_grabed  = None
        self.__color = color
        self.__list_teboka = []
        
    def getColor (self):
        return self.__color
    def setColor (self , color:str):
        self.__color = color
        
    def getListTeboka  (self):
        return self.__list_teboka
    
    def copyKo(self):
        copied_player = Player(self.__id_player, self.__color)
        copied_player.setScore(self.__score)

        if self.__teboka_grabed:
            copied_player.setTebokaGrabed(self.__teboka_grabed.copyKo())

        copied_player.__list_teboka = [teboka.copyKo() for teboka in self.__list_teboka]

        return copied_player
    
        
        
        
    
    def getTebokaGrabed (self):
        return self.__teboka_grabed
    def setTebokaGrabed (self , teboka:Teboka):
        self.__teboka_grabed = teboka
    
    
    def setTeboka (self , teboka:Teboka):
        self.__list_teboka = teboka
        
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
        points:list[Point] = []
        for teboka in self.__list_teboka:
            points.append(teboka.getPoint())
        return points

    def getScore (self):
        return self.__score
    def setScore (self , score):
        self.__score = score
    
    def checkWin (self):
        teboka_point = self.getTebokaPoints()
        if  len (teboka_point) ==3:
            return Fonction.sont_colineaires(teboka_point)
        return False
        
        
   
    
    
        