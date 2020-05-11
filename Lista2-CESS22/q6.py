from __future__ import division

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def slope_from_origin(self):
        return self.y/self.x

P = Point(3,5)
print(P.slope_from_origin())
print("Esse metodo falha quando ocorre divisao por 0, ou seja, quando P esta no eixo Y.")