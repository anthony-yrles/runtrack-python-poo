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
    
rectangle = Rectangle(20, 15)
print(rectangle.aire())
rectangle.aire()
print(rectangle.aire())