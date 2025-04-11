from datetime import date
import tkinter as tk
from tkinter import messagebox
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
    current_node:Node =  Node(None , Data.players , Data.indexs_tour  , Data.table.getBoxs() , generation=0)
    if current_node:
      current_node.miteraka(0)
      # current_node.toString()
      
      for nodes in current_node.getChildren():
        nodes.toString()
      
    else:
      print("Pas de node pour l'instant")
