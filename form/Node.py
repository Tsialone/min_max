from datetime import time
from objets.Player import Player
from form.Teboka import Teboka

from fonction.Data import Data
from fonction.Fonction import Fonction

import copy


# objet_clone = copy.deepcopy(mon_objet)
class Node:
    nodes_founds = []

    def __init__(self, parent, list_player, index_tour, list_boxs, generation):
        self.__children = []
        self.__generation = generation
        self.__index_tour = copy.deepcopy(index_tour)
        self.setBoxs(copy.deepcopy(list_boxs))
        self.__list_player = copy.deepcopy(list_player)
        self.__parent = parent

   
        
        
    def getBoxs(self):
        return self.__boxs

    def setBoxs(self, list__box):
        self.__boxs = list__box

    def getGeneration(self):
        return self.__generation

    def setGeneration(self, generation):
        self.__generation = generation

    def copyPlayer(self, list_player):
        for player in list_player:
            self.__list_player.append(player)

    def getIndexTour(self):
        return self.__index_tour

    def setIndexTour(self, index):
        self.__index_tour = index

    def getTable(self):
        return self.__table

    def setTable(self, table):
        self.__table = table

    def addChild(self, node_child):
        self.__children.append(node_child)

    def getParent(self):
        return self.__parent

    def setParent(self, parent):
        self.__parent = parent

    def getChildren(self):
        return self.__children

    def getListPlayer(self):
        return self.__list_player

    def setListPlayer(self, list):
        self.__list_player = list
    
    
        
    

    def toString(self):
        print("\n---------------")
        print(f"generation: {self.getGeneration()}")
        print(f"index_tour: {self.getIndexTour()}")
        print(f"placer_par 1:{self.getListPlayer()[0].getTebokaPoints()} score: {self.getListPlayer()[0].getScore()}")
        print(f"placer_par 2:{self.getListPlayer()[1].getTebokaPoints()} score: {self.getListPlayer()[1].getScore()}")
        print(f"place_dispo: {self.getPlaceDispo()}")
        print(f"nbr_child: {len(self.getChildren())}")
        
        print("---------------")
        with open("output.txt", "a") as file:
            file.write("\n---------------\n")
            file.write(f"generation: {self.getGeneration()}\n")
            file.write(f"index_tour: {self.getIndexTour()}\n")
            file.write(f"placer_par 1: {self.getListPlayer()[0].getTebokaPoints()} score: {self.getListPlayer()[0].getScore()}\n")
            file.write(f"placer_par 2: {self.getListPlayer()[1].getTebokaPoints()} score: {self.getListPlayer()[1].getScore()} \n")
            file.write(f"place_dispo: {self.getPlaceDispo()}\n")
            file.write(f"nbr_child: {len(self.getChildren())}\n")
            file.write("---------------\n")

    def getPlaceDispo(self):
        all_box = self.getBoxs()
        all_point_players = []
        for player in self.__list_player:
            all_point_players.extend(player.getTebokaPoints())
        all_point_dispo = []
        for box in all_box:
            if box.getPoint() not in all_point_players:
                all_point_dispo.append(box.getPoint())
                
         
        #noires       
        result  = [pt for pt in  all_point_dispo if pt not in Data.point_noires ]
        return result
        # return all_point_dispo
    

    
    def attributScore (self):
        if ( self.__list_player[self.getIndexTour()[0]].checkWin() ):
                self.__list_player[self.getIndexTour()[0]].setScore(1)
                self.__list_player[self.getIndexTour()[1]].setScore(-1)
        elif ( self.__list_player[self.getIndexTour()[1]].checkWin() ):
            self.__list_player[self.getIndexTour()[1]].setScore(1)
            self.__list_player[self.getIndexTour()[0]].setScore(-1)
        else: 
                self.__list_player[self.getIndexTour()[0]].setScore(0)
                self.__list_player[self.getIndexTour()[1]].setScore(0)
    
    def miteraka(self, depth):
        if (
            self.__list_player[self.getIndexTour()[0]].checkWin()
            or self.__list_player[self.getIndexTour()[1]].checkWin()
            or depth == Data.profondeur
        ):
            self.attributScore()
            # self.getIndexTour().reverse()
            Data.terminal_node.append(self)
            return
        
        if self.getParent():
            self.getIndexTour().reverse()
            
        all_point_dispo = self.getPlaceDispo()
        # self.__index_tour.reverse()
        for point in all_point_dispo:
            temp_node = Node(
                self,
                self.__list_player,
                self.__index_tour,
                self.getBoxs(),
                self.getGeneration() + 1,
            )
            temp_node_liste_player = temp_node.getListPlayer()
            index_tour = temp_node.getIndexTour()[0]
            # raise Exception(f"hahaha: {index_tour}")
            player_tour: Player = temp_node_liste_player[index_tour]
            nbr_points_player = len(player_tour.getTebokaPoints())
            if nbr_points_player < 3:
                teboka = Teboka(point=point, couleur=player_tour.getColor())
                player_tour.addTeboka(teboka=teboka)
                self.addChild(temp_node)
                temp_node.miteraka(depth + 1)
                
            else:
                
                teboka_hakisako = []
                for player_teboka in player_tour.getListTeboka():
                    if Fonction.estProche(player_teboka.getPoint() , point) and point in player_teboka.getAzoAleha():
                        teboka_hakisako.append(player_teboka)
                # print(f"point: {point} ")
                for teboka_findra in teboka_hakisako:
                    # print(f"teboka_hakisaka: {teboka_findra.getPoint()}")
                    teboka_initial = copy.deepcopy(teboka_findra)
                    teboka_findra.setPoint(point) 
                    temp_node_3 = Node(
                       self,
                       temp_node_liste_player,
                       temp_node.getIndexTour(),
                       self.getBoxs(),
                       self.getGeneration() + 1,
                   )
                    self.addChild(temp_node_3)
                    temp_node_3.miteraka(depth + 1)                    
                    teboka_findra.setPoint(teboka_initial.getPoint ())
                 
                
        # self.toString() 
       
      
