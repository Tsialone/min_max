import math
from  form.Point import Point
import time
class Fonction:
    def sont_colineaires(points: list[Point], epsilon=1e-6) -> bool:
        if len(points) < 3:
            return True

        x0, y0 = points[0].x, points[0].y
        x1, y1 = points[1].x, points[1].y

        for i in range(2, len(points)):
            xi, yi = points[i].x, points[i].y
            det = (x1 - x0)*(yi - y0) - (y1 - y0)*(xi - x0)
            # print(f"Déterminant avec P0, P1, P{i} = {det}")
            if abs(det) > epsilon:
                return False

        return True

    def distance(point1:Point, point2:Point):
        x1 = point1.x
        y1 = point1.y
        
        x2 = point2.x
        y2 = point2.y
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    def getProche (point:Point, list_points:list):
        eps = 50
        for point_temp in list_points:
            distance = Fonction.distance(point_temp, point)
            if distance < eps:
                return point_temp
        return None
    
    def estProche (a:Point , b:Point):
        distance  = a.distance(b)
        return distance <= 396
    
    def min_max (etat  ,  profondeur , estMax  , deep):
        from fonction.Data import Data
        if profondeur == Data.profondeur or etat in Data.terminal_node :
            etat.attributScore()
            # his_v = etat.getListPlayer()[Data.indexs_tour[0]].getScore()  / deep
            sign = 1 if etat.getListPlayer()[Data.indexs_tour[0]].getScore() >= 0 else -1
            his_v = etat.getListPlayer()[Data.indexs_tour[0]].getScore() + sign * (1 / deep)  
            return his_v
        if estMax:
            v =  float("-inf")
            for child in etat.getChildren():
                child.deep = deep + 1
                v = max(v , Fonction.min_max (child , profondeur+1 , False  ,deep+1  ))
            etat.getListPlayer()[Data.indexs_tour[0]].setScore(v)
            return v
        else:
            v=float("+inf")
            for child in etat.getChildren():
                child.deep = deep + 1
                v = min(v , Fonction.min_max (child , profondeur+1 , True  , deep + 1))
            etat.getListPlayer()[Data.indexs_tour[0]].setScore(v) 
            return v 
    def getAzoAleha (his_point:Point):
        from fonction.Data import Data
        result  = [pt for pt in  Data.moves.get(his_point, []) if pt not in Data.point_noires ]
        return result
    
    def getMaxNode(nodes):
        from fonction.Data import Data

        # start_time = time.time()  # ⏱️ Start timer

        max_node = None
        max_score = float("-inf")
        for node in nodes:
            score = node.getListPlayer()[Data.indexs_tour[0]].getScore()
            if score > max_score:
                max_score = score
                max_node = node

        # end_time = time.time()  # ⏱️ End timer

        # print(f"[TIMER] getMaxNode executed in {end_time - start_time:.6f} seconds")

        return max_node
        
        
        