class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def reflect_x(self):
        return Point(self.x,-self.y)

P = Point(3,5)
print(P.reflect_x().x, P.reflect_x().y)