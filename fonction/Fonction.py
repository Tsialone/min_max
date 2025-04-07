import math
from shapely.geometry import Point


class Fonction:
    def sont_colineaires(points: list[Point], epsilon=1e-6) -> bool:
        if len(points) < 3:
            return True

        x0, y0 = points[0].x, points[0].y
        x1, y1 = points[1].x, points[1].y

        for i in range(2, len(points)):
            xi, yi = points[i].x, points[i].y
            det = (x1 - x0)*(yi - y0) - (y1 - y0)*(xi - x0)
            print(f"Déterminant avec P0, P1, P{i} = {det}")
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