from form.Node import Node
import copy

class Graphe:
    origin_node:Node = None
    
    def drawGraph ():
        temp = copy.deepcopy(Graphe.origin_node)
        temp.toString()
        while temp.getChildren():
            for child_node in temp.getChildren():
                child_node.toString()
        
            
            
        
    
    
    
    