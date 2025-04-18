from tkinter import messagebox
from form.Point import Point
from fonction.Fonction import Fonction
from objets.Box import Box
from fonction.Data import Data
from form.Teboka import Teboka
from form.Node import Node


import math


class Mouse:
    gauche: Point = None
    droite: Point = None

    @staticmethod
    def deplacePoint(event, list_box, table):
        index_tour = Data.indexs_tour[0]
        player_deplace = Data.players[index_tour]
        player_tebokas = player_deplace.getListTeboka()
        all_tebokas_point = []
        for teboka in player_tebokas:
            all_tebokas_point.append(teboka.getPoint())


        Mouse.gauche = Point(event.x, event.y)
        eps: float = 50
        table_canvas = table.getCanvas()
        for box in list_box:
            temp_box: Box = box
            temp_box_point = Point(temp_box.x, temp_box.y)
            
            #noires
            if temp_box_point in Data.point_noires:
                continue

            distance = Fonction.distance(Mouse.gauche, temp_box_point)
            if distance < eps:
                player_teboka = Teboka(temp_box_point, player_deplace.getColor())
                id = str(temp_box_point.x) + "-" + str(temp_box_point.y)
                point_taged = table_canvas.find_withtag(id)
                if not point_taged and len(player_tebokas) < 3:
                    player_deplace.addTeboka(player_teboka)
                    table.drawPoint(point=temp_box_point, color=player_deplace.getColor())
                    print(f"Player: {player_deplace.getIdPlayer()} a place un point: {temp_box_point}")
                    # print(Data.indexs_tour)
                    
                    # Data.current_node = Node(None , Data.players , Data.indexs_tour  , table.getBoxs() , generation=0)
                    # print(player_deplace.checkWin())
                    if (player_deplace.checkWin()):
                        table.drawWin(player_deplace.getTebokaPoints() , player_deplace.getColor())
                        messagebox.showinfo("click", f"Player: {player_deplace.getIdPlayer()} a gagner")
                        break
                    Data.indexs_tour.reverse()
                    # print("debug"  , Data.indexs_tour)
                    break
                else:
                    if len(player_tebokas) >= 3:
                        # print(f"{(all_tebokas_point)}")
                        if (player_teboka.getPoint() in all_tebokas_point):
                            player_deplace.setTebokaGrabed(player_teboka)
                            print(f"Player: {player_deplace.getIdPlayer()} a choisi un point a deplacer: {temp_box_point}")
                            break
                        # messagebox.showinfo("click", f"efa misy point mipetraka: {temp_box_point}")

    @staticmethod
    def placePoint(event, list_box, table):
        index_tour = Data.indexs_tour[0]
        # print("click droite")
        player_deplace = Data.players[index_tour]
        teboka_grabed = player_deplace.getTebokaGrabed()
        if not teboka_grabed:
            messagebox.showinfo("click", f"Vous n'avez pas graber un vato")
            return

        player_tebokas = player_deplace.getListTeboka()
        list_point_box = []
        for box in list_box:
            temp_box: Box = box
            temp_box_point = Point(temp_box.x, temp_box.y)
            list_point_box.append(temp_box_point)


        # print(f"Player_tour: {player_deplace.getIdPLayer()}")

        Mouse.droite = Point(event.x, event.y)
        eps: float = 50
        table_canvas = table.getCanvas()
        for box in list_box:
            temp_box: Box = box
            temp_box_point = Point(temp_box.x, temp_box.y)
            
            #noires
            if temp_box_point in Data.point_noires:
                continue
            
            distance = Fonction.distance(Mouse.droite, temp_box_point)
            if distance < eps:
                player_teboka = Teboka(temp_box_point, player_deplace.getColor())
                player_teboka_grabed = player_deplace.getTebokaGrabed()
                id = str(temp_box_point.x) + "-" + str(temp_box_point.y)
                point_taged = table_canvas.find_withtag(id)
                mouse_reference = Fonction.getProche(Mouse.droite, list_point_box)
                
                # print(f"in: {mouse_reference  in   player_teboka_grabed.getAzoAleha()} mouse: {mouse_reference} liste: {player_teboka_grabed.getAzoAleha()}  ")
                if not point_taged and mouse_reference in Fonction.getAzoAleha(player_teboka_grabed.getPoint()):
                    print(temp_box_point)
                    print(f"avant: { player_deplace.getTebokaPoints() }")
                    player_deplace.removeTeboka(teboka_grabed)
                    player_deplace.addTeboka(player_teboka)
                    table.deleteOval(teboka_grabed.getPoint())
                    print(f"apres: { player_deplace.getTebokaPoints() }")
                    table.drawPoint(point=temp_box_point, color=player_deplace.getColor())
                    player_deplace.setTebokaGrabed(None)
                    print(f"Player: {player_deplace.getIdPlayer()} a deplacer un point: {temp_box_point}")
                    print(player_deplace.checkWin())
                    if (player_deplace.checkWin()):
                        table.drawWin(player_deplace.getTebokaPoints() , player_deplace.getColor())
                        messagebox.showinfo("click", f"Player: {player_deplace.getIdPlayer()} a gagner")
                        break
                    Data.indexs_tour.reverse()
                    print(f"{Data.indexs_tour}")
                    break
