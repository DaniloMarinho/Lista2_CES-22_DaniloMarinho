from __future__ import division

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def get_line_to(self, P):
        m = (P.y-self.y)/(P.x-self.x)
        c = self.y - m*self.x
        return (m,c)

P = Point(1,12)
Q = Point(-1,-12)
print(P.get_line_to(Q))