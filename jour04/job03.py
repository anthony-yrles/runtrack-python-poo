class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def set__longueur(self, longueur):
        self.__longueur = longueur
    def get__longueur(self):
        return self.__longueur
    
    def set__largeur(self, largeur):
        self.__largeur = largeur
    def get__largeur(self):
        return self.__largeur

    def perimetre(self):
        return self.get__longueur() * 2 + self.get__largeur() * 2

    def surface(self):
        return self.get__longueur() * self.get__largeur()
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur
    
    def get__hauteur(self):
        return self.__hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.get__longueur() * self.get__largeur() * self.get__hauteur()
    
parallelepipede = Parallelepipede(10, 5, 50)
peri = parallelepipede.perimetre()
surf = parallelepipede.surface()
vol = parallelepipede.volume()
print(f'Perimetres = {peri} \nSurface = {surf} \nVolume = {vol}')