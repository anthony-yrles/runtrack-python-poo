class Livre:
    def __init__(self, titre, auteur, number_of_page, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__number_of_page = number_of_page
        self.__disponible = disponible
    def set__titre(self, titre):
        self.__titre = titre
    def set__auteur(self, auteur):
        self.__auteur = auteur
    def set__number_of_page(self, number_of_page):
        if isinstance(number_of_page, int) and number_of_page >= 1:
            self.__number_of_page = number_of_page
        else:
            print('Le nombre de page doit être un entier positif')
    def set__disponible(self, disponible):
        if disponible:
            self.__disponible = False
        else:
            self.__disponible = True
    def get__titre(self):
        return self.__titre
    def get__auteur(self):
        return self.__auteur
    def get__number_of_page(self):
        return self.__number_of_page
    def get__disponible(self):
        return self.__disponible
    def verification(self):
        if self.get__disponible():
            return True
        return False
    def emprunter(self):
        if self.verification():
            self.set__disponible(self.__disponible)
    def rendre(self):
        if not self.verification():
            self.set__disponible(self.__disponible)

livre = Livre('Jujutsu Kaisen', 'Gege', 400)
print(f"L'auteur du livre {livre.get__titre()} est {livre.get__auteur()} et fais {str(livre.get__number_of_page())} pages et le livre est disponible = {livre.get__disponible()}")
livre.emprunter()       
print(f"L'auteur du livre {livre.get__titre()} est {livre.get__auteur()} et fais {str(livre.get__number_of_page())} pages et le livre est disponible = {livre.get__disponible()}")
livre.rendre()
print(f"L'auteur du livre {livre.get__titre()} est {livre.get__auteur()} et fais {str(livre.get__number_of_page())} pages et le livre est disponible = {livre.get__disponible()}")