import math
from form.Point import Point
class Teboka:
    def __init__ (self,  point:Point , couleur:str):
        self.__point = point
        self.__couleur = couleur
        
    def getCouleur (self):
        return self.__couleur
    def setCouleur (self , couleur:str):
        self.__couleur = couleur
        
    def getPoint (self):
        return self.__point
    def setPoint (self , point:Point):
        self.__point =  point
    
    def copyKo(self):
        return Teboka(
            point=self.__point,  
            couleur=self.__couleur
        )
    # def getAzoAleha(self):
    #     his_point = self.getPoint()
    #     moves = {
    #         Point(135, 135): [Point(135, 415), Point(415, 135), Point(415, 415)],
    #         Point(415, 135): [Point(135, 135), Point(695, 135), Point(415, 415)],
    #         Point(695, 135): [Point(695, 415), Point(415, 135), Point(415, 415)],

    #         Point(135, 415): [Point(135, 135), Point(135, 695), Point(415, 415)],
    #         Point(415, 415): [
    #             Point(135, 135), Point(415, 135), Point(695, 135),
    #             Point(135, 415), Point(695, 415),
    #             Point(135, 695), Point(415, 695), Point(695, 695)
    #         ],
    #         Point(695, 415): [Point(695, 135), Point(695, 695), Point(415, 415)],

    #         Point(135, 695): [Point(135, 415), Point(415, 415), Point(415, 695)],
    #         Point(415, 695): [Point(135, 695), Point(695, 695), Point(415, 415)],
    #         Point(695, 695): [Point(415, 695), Point(695, 415), Point(415, 415)],
    #     }
        
        
    #     #noires
    #     from fonction.Data import Data
    #     result  = [pt for pt in  moves.get(his_point, []) if pt not in Data.point_noires ]
    #     return result
        # if  ():
            
        
        
        
    
    
   
        