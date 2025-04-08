from objets.Player import Player
class Node:
    def __init__ (self , parent, list_player):
        self.__children =  []
        self.__list_player = []
        self.copyPlayer(list_player=list_player)
        self.__parent  = parent
        
    def addChil (self,node_child):
        self.__children.append(node_child)
    
    def getParent (self):
        return self.__parent
    
    def setParent (self , parent):
        self.__parent = parent
        
    def getChildren (self):
        return self.__children
    
    def copyPlayer(self , list_player):
        for player in list_player:
            temp_player = Player(player.getIdPlayer() , player.getColor())
            self.__list_player.append(temp_player)
    
    # def extendChild():
        
        
    
    
        