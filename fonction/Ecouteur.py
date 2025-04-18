import cProfile
from datetime import date
import io
import pstats
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
    # if (len(Data.players[0].getListTeboka()) + len(Data.players[1].getListTeboka())) <  4:
      # Data.profondeur = 3
    # else:
      # Data.profondeur = 6
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
    import time

    start = time.perf_counter()


    try:
        current_node: Node = Node(None, Data.players, Data.indexs_tour, Data.table.getBoxs(), generation=0)
        point_hita= None

        if current_node:
            profiler = cProfile.Profile()
            profiler.enable()

            # 🔽 Appel de ta fonction lente ici
            current_node.miteraka(0)

            profiler.disable()

            # 🔽 Affichage lisible dans la console
            s = io.StringIO()
            sortby = "tottime"  # ou "cumulative"
            ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
            ps.print_stats(20)  # Affiche les 20 fonctions les plus coûteuses
            print(s.getvalue())
            score_minmax = Fonction.min_max(current_node, 0, True , 0)
            max_node =  Fonction.getMaxNode (current_node.getChildren())
            if max_node:
              point_hita = max_node.getListPlayer()[Data.indexs_tour[0]].getTebokaPoints()
              print(f"testttttt:  {max_node.getListPlayer()[Data.indexs_tour[0]].getScore()}")
              for xx in point_hita:
                  print(xx)
              
            # for child in current_node.getChildren():
            #     # child.toString()
            #     score = child.getListPlayer()[Data.indexs_tour[0]].getScore()
              
            #     player_point = child.getListPlayer()[Data.indexs_tour[0]].getTebokaPoints()
                
            #     # if score == score_minmax:
            #     print("nahita\n")
            #     for xx in player_point:
            #       print(xx)
            #     print(f"score_noeud: {score}")
            #     print(f"node_deep: {child.deep}")
            #     print(f"score_min_max: {score_minmax}")
            #     # if score == score_minmax:
            #       # point_hita = child.getListPlayer()[Data.indexs_tour[0]].getTebokaPoints()
            #       # print(f"score_noeud: {score}")
            #       # print(f"score_min_max: {score_minmax}")
            #       # break 
                  
            #     # break

        def mise_a_jour_tk():
            popup.destroy()
            if point_hita:
                the_player = Data.players[Data.indexs_tour[0]]
                ancient_point = the_player.getTebokaPoints()
                for point in ancient_point:
                    Data.table.deleteOval(point)
                from form.Teboka import Teboka
                new_teboka = []
                for point in point_hita:
                    new_teboka.append(Teboka(point, the_player.getColor()))
                the_player.setTeboka(new_teboka)

                for teboka_point in the_player.getTebokaPoints():
                    Data.table.drawPoint(teboka_point, the_player.getColor())
                if the_player.checkWin():
                    Data.table.drawWin(the_player.getTebokaPoints(), the_player.getColor())
                    messagebox.showinfo("click", f"Player: {the_player.getIdPlayer()} a gagner")
                Data.indexs_tour.reverse()

            end = time.perf_counter()
            print(f"Temps écoulé : {end - start:.4f} secondes")
            
            
            # Data.terminal_node.clear()

        Data.table.after(0, mise_a_jour_tk)

    except Exception as e:
        print("Erreur pendant traitement :", e)
        traceback.print_exc()
        
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
      
   
