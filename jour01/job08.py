import math

class Cercle:
    def __init__(self):
        self.rayon = 5
    def changerRayon(self):
        self.rayon = float(input())
    def afficherInfos(self):
        print(f"Le Rayon est {self.rayon}, la circonférence est {self.circonference()}, l'aire est {self.aire()}, le diametre est {self.diametre()}")
    def circonference(self):
        circonf = (self.rayon ** 2) * math.pi
        return circonf
    def aire(self):
        air = self.rayon**2 * math.pi
        return air
    def diametre(self):
        diam = self.rayon * 2
        return diam

cercle = Cercle()
print(cercle.rayon)
cercle.changerRayon()
cercle.circonference()
cercle.aire()
cercle.diametre()
print(cercle.afficherInfos())