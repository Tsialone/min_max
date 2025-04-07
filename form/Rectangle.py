import tkinter as tk
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
      

    def draw(self, canvas:tk.Canvas):
        canvas.create_rectangle(
            self.x + 1, self.y+1, self.x + self.width, self.y + self.height,
         outline="black" 
        ) 