class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def gauche(self):
        self.x -= 1
    def droite(self):
        self.x += 1
    def haut(self):
        self.y -= 1
    def bas(self):
        self.y += 1
    def position(self):
        return([self.x, self.y])

personnage = Personnage(5, 12)
personnage.gauche()
personnage.gauche()
personnage.gauche()
personnage.gauche()
personnage.droite()
personnage.haut()
personnage.haut()
personnage.haut()
personnage.haut()
personnage.bas()
print(f"Déplacement en x vers {personnage.position()}")
