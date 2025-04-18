import tkinter as tk
import display.Fenetre as Fn
from objets.Box import Box
from form.Point import Point
from fonction.Mouse import Mouse


class Table(tk.Frame):
    def __init__(self, width: int, height: int, parent: Fn.Fenetre , afficher:bool):
        super().__init__(parent, bg="lightblue", width=width, height=height)
        self.pack_propagate(False)
        self.__canvas = None
        if afficher:
            self.place(x=10, y=10)
        self.__boxs = []
        self.__parent = parent
        self.update_idletasks()
        self.initBoxs()
        self.drawTsipika()

    def getParent (self):
        return self.__parent
        
    def getBoxs(self):
        return self.__boxs

    def setBoxs(self, boxs):
        self.__boxs = boxs

    def getCanvas(self):
        return self.__canvas

    def initBoxs(self):
        temp_x = 0
        temp_y = 0
        x_max = self.winfo_width()
        y_max = self.winfo_height()
        # print(f"x_max: {x_max} y_max: {y_max}")
        nbr_box = 9
        margin_right = 270
        margin_top = 270

        self.__canvas = tk.Canvas(
            self,
            width=x_max - 40,
            height=y_max - 20,
            bg="white",
        )

        self.__canvas.place(x=self.winfo_x(), y=self.winfo_y())

        for i in range(nbr_box):
            # print(f"tempx: {temp_x} , temp_y: {temp_y}")
            temp_box = Box(temp_x, temp_y, i + 1, margin_right, margin_top)
            temp_box.draw(self.__canvas)

            center_x = temp_x + (margin_right / 2)
            center_y = temp_y + (margin_top / 2)

            # self.drawPoint(point=Point(center_x, center_y), color="red")
            temp_box.x = center_x
            temp_box.y = center_y
            self.__boxs.append(temp_box)
            self.__canvas.create_text(
                center_x, center_y - 50, text=str(center_x) + "-" + str(center_y)
            )

            temp_x += margin_right + 10
            if temp_x + margin_right >= x_max:
                temp_x = 0
                temp_y += margin_top + 10
            if temp_y + margin_top >= y_max:
                temp_y = 0
        self.__canvas.bind(
            "<Button-1>",
            lambda event: Mouse.deplacePoint(event, list_box=self.__boxs, table=self),
        )
        self.__canvas.bind(
            "<Button-3>",
            lambda event: Mouse.placePoint(event, list_box=self.__boxs, table=self),
        )

        self.update()

    def drawPoint(self, point: Point, color: str):
        self.__canvas.create_oval(
            point.x - 15,
            point.y - 15,
            point.x + 15,
            point.y + 15,
            fill=color,
            outline="black",
            tags=str(point.x) + "-" + str(point.y),
        )

    def deleteOval(self, point: Point):
        self.__canvas.delete(str(point.x) + "-" + str(point.y))

    def drawTsipika(self):
        # ligne 1
        self.__canvas.create_line(135, 135, 695, 135, fill="black" , width=5)
        # ligne 2
        self.__canvas.create_line(695, 135, 695, 695, fill="black" , width=5)
        # ligne 3
        self.__canvas.create_line(135, 135, 135, 695, fill="black" , width=5)
        # ligne 4
        self.__canvas.create_line(135, 415, 695, 415, fill="black" , width=5)
        # ligne 5
        self.__canvas.create_line(135, 695, 695, 695, fill="black" , width=5)
        # ligne 6
        self.__canvas.create_line(135, 135, 695, 695, fill="black" , width=5)
        # ligne 7
        self.__canvas.create_line(695, 135, 135, 695, fill="black" , width=5)
        # ligne 8
        self.__canvas.create_line(415, 135, 415, 695, fill="black" , width=5)
    def drawWin(self, liste_point , color:str):
        if len(liste_point) < 2:
            return 
        for i in range(len(liste_point) - 1):
            p1 = liste_point[i]
            p2 = liste_point[i + 1]
            self.__canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=color, width=5)
            
            
            
        