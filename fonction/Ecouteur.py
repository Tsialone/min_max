from datetime import date
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import traceback
from fonction.Data import Data
from fonction.Fonction import Fonction
from form.Node import Node
import pyodbc
from decimal import Decimal, getcontext
getcontext().prec = 10


class Ecouteur:
  @staticmethod
  def direBonjour():
    print("Bonjour")
  @staticmethod
  def generer():
    # current_node:Node =  Node(None , Data.players , Data.indexs_tour  , Data.table.getBoxs() , generation=0)
    # player_point = None
    # if current_node:
      # current_node.miteraka(0)
      # score_minmax = Fonction.min_max(current_node , 0 , True)
      
      
    Ecouteur.lancer_calcul()
      # for child in current_node.getChildren():
      #   score =   child.getListPlayer()[Data.indexs_tour[0]].getScore()
      #   if score == score_minmax:
      #     player_point = child.getListPlayer()[Data.indexs_tour[0]].getTebokaPoints()
      #     print(f"nahita: {player_point}")
      #     print(f"score: {score_minmax}")
      #     break
        
      # if player_point:
      #   the_player = Data.players[Data.indexs_tour[0]]
      #   ancient_point = the_player.getTebokaPoints()
      #   for point in ancient_point:
      #     Data.table.deleteOval(point)
      #   from form.Teboka import Teboka
      #   new_teboka = []
      #   for point in player_point:
      #     new_teboka.append( Teboka  (point , the_player.getColor() ))
      #   the_player.setTeboka(new_teboka)
        
      #   for teboka_point in the_player.getTebokaPoints():
      #     Data.table.drawPoint(teboka_point , the_player.getColor())
      #   if (the_player.checkWin()):
      #       Data.table.drawWin(the_player.getTebokaPoints() , the_player.getColor())
      #       messagebox.showinfo("click", f"Player: {the_player.getIdPlayer()} a gagner")
      #   Data.indexs_tour.reverse()
        
      # Data.terminal_node.clear()
  def traitement_et_fermer_popup(popup):
    current_node:Node =  Node(None , Data.players , Data.indexs_tour  , Data.table.getBoxs() , generation=0)
    player_point = None

    if current_node:
        current_node.miteraka(0)
        score_minmax = Fonction.min_max(current_node, 0, True)

        for child in current_node.getChildren():
            score = child.getListPlayer()[Data.indexs_tour[0]].getScore()
            if score == score_minmax:
                player_point = child.getListPlayer()[Data.indexs_tour[0]].getTebokaPoints()
                print(f"nahita: {player_point}")
                print(f"score: {score_minmax}")
                break
    popup.destroy()
    if player_point:
        the_player = Data.players[Data.indexs_tour[0]]
        ancient_point = the_player.getTebokaPoints()
        for point in ancient_point:
          Data.table.deleteOval(point)
        from form.Teboka import Teboka
        new_teboka = []
        for point in player_point:
          new_teboka.append( Teboka  (point , the_player.getColor() ))
        the_player.setTeboka(new_teboka)
        
        for teboka_point in the_player.getTebokaPoints():
          Data.table.drawPoint(teboka_point , the_player.getColor())
        if (the_player.checkWin()):
            Data.table.drawWin(the_player.getTebokaPoints() , the_player.getColor())
            messagebox.showinfo("click", f"Player: {the_player.getIdPlayer()} a gagner")
        Data.indexs_tour.reverse()
        
    Data.terminal_node.clear()
  def lancer_calcul():
    popup = tk.Toplevel(Data.table)
    popup.title("Chargement en cours")
    popup.geometry("300x100")
    ttk.Label(popup, text="Thinking...").pack(pady=20)
    progress = ttk.Progressbar(popup, mode="indeterminate")
    progress.pack(pady=5)
    progress.start()
    thread = threading.Thread(target=Ecouteur.traitement_et_fermer_popup, args=(popup,))
    thread.start()
      
   
