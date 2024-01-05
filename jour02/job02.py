class Livre:
    def __init__(self, titre, auteur, number_of_page):
        self.__titre = titre
        self.__auteur = auteur
        self.__number_of_page = number_of_page
    def set__titre(self, titre):
        self.__titre = titre
    def set__auteur(self, auteur):
        self.__auteur = auteur
    def set__number_of_page(self, number_of_page):
        if isinstance(number_of_page, int) and number_of_page >= 1:
            self.__number_of_page = number_of_page
        else:
            print('Le nombre de page doit être un entier positif')
    def get__titre(self):
        return self.__titre
    def get__auteur(self):
        return self.__auteur
    def get__number_of_page(self):
        return self.__number_of_page
    
livre = Livre('Jujutsu Kaisen', 'Gege', 400)
print(f"L'auteur du livre {livre.get__titre()} est {livre.get__auteur()} et fais {str(livre.get__number_of_page())} pages")
livre.set__auteur('Echiro Oda')
livre.set__titre('One piece')
livre.set__number_of_page(4.3)
livre.set__number_of_page(8)
print(f"L'auteur du livre {livre.get__titre()} est {livre.get__auteur()} et fais {str(livre.get__number_of_page())} pages")