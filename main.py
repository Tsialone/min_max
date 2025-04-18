import numpy as np
# from shapely.geometry import Point
from form.Point import Point
import shapely
import copy

test = np.array(
    [
    [Point(1, 2), Point(3, 4)],
        [Point(12, 12), Point(3, 2)],
        [Point(12, 12), Point(3, 2)],
        
    ]
)

list_point = [
    Point(135 , 135),
    Point(415 , 135),
    Point(695 , 135),
    
    Point(135 , 415),
    Point(415 , 415),
    Point(695 , 415),
    
    Point(135 , 695),
    Point(415 , 695),
    Point(695 , 695),
]

test[0, 0] = Point(100, 200)
temp =  [
    (100 , 100),
    (103 , 120),
    (101 , 110),
    (100 , 108)
    
]

a = Point(135  , 135)
b = Point(135  , 415)


temp = [
    a , 
    b
]
print(Point(135 , 135) in temp)


# for i in range  (0 , 2_000_000):
#     copie =  test.copy()
#     point =Point(100 ,100)
#     temp.append(point)
#     # copie =   copy.deepcopy (test)
#     # temp.reverse()
#     # temp.append(copie)

# print( len (temp))