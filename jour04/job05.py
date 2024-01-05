class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def set__largeur(self, largeur):
        self.__largeur = largeur
    def get__largeur(self):
        return self.__largeur
    
    def set__hauteur(self, hauteur):
        self.__hauteur = hauteur
    def get__hauteur(self):
        return self.__hauteur
    
    def aire(self):
        return self.__hauteur * self.__largeur
    
class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
    
    def set__radius(self, radius):
        self.__radius = radius
    
    def get__radius(self):
        return self.__radius
    
    def aire(self):
        return self.__radius * 3.14216
    
rectangle = Rectangle(20, 15)
rectangle.aire()
print(rectangle.aire())
cercle = Cercle(6)
cercle.aire()
print(cercle.aire())