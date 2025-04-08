class Graphe:
    def __init__ (self , id_graphe):
        self.__id_graphe = id_graphe
        self.__nodes =  []
        
    def getIdGraphe (self):
        return self.__id_graphe
    def setIdGraphe  (self , id_graphe):
        self.__id_graphe = id_graphe
        
    def getNodes (self):
        return self.__nodes
    def addNode (self , node):
        self.__nodes.append(node)
    
    
    