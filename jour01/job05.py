class Point:
    def __init__(self):
        self.x = 5
        self.y = 8
    def afficherLesPoints(self, x, y):
        print(x, y)
    def afficherX(self, x):
        print(x)
    def afficherY(self, y):
        print(y)
    def changerX(self, x):
        x = input()
        print(x)
    def changerY(self, y):
        y = input()
        print(y)

p = Point()
p.afficherLesPoints(p.x, p.y)
p.afficherX(p.x)
p.afficherY(p.y)
p.changerX(p.x)
p.changerY(p.y)