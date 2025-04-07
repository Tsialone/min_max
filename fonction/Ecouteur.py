from datetime import date
import tkinter as tk
from tkinter import messagebox
import traceback
from fonction.Data import Data
from fonction.Fonction import Fonction
import pyodbc
from decimal import Decimal, getcontext
getcontext().prec = 10


class Ecouteur:
  @staticmethod
  def direBonjour():
    print("Bonjour")
