class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def get__longueur(self):
        return self.__longueur
    def get__largeur(self):
        return self.__largeur
    def set__longueur(self, longueur):
        self.__longueur = longueur
    def set__largeur(self, largeur):
        self.__largeur = largeur

rectangle = Rectangle(10, 5)
print(rectangle.get__longueur(), rectangle.get__largeur())
rectangle.set__longueur(23)
rectangle.set__largeur(8)
print(rectangle.get__longueur(), rectangle.get__largeur())