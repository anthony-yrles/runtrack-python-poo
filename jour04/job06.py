class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix
    
    def set__marque(self, marque):
        self.__marque = marque
    def get__marque(self):
        return self.__marque
    
    def set__modele(self, modele):
        self.__modele = modele
    def get__modele(self):
        return self.__modele
    
    def set__annee(self, annee):
        self.__annee = annee
    def get__annee(self):
        return self.__annee
    
    def set__prix(self, prix):
        self.__prix = prix
    def get__prix(self):
        return self.__prix
    
    def informationsVehicule(self):
        print(f'La voiture de marque {self.__marque} est de modèle {self.__modele} sortit en {self.__annee} au prix de {self.__prix} €')
    
    def demarrer(self):
        print('Attention, je demarre')
    
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.__portes = portes
    
    def set__portes(self, portes):
        self.__portes = portes
    def get__portes(self):
        return self.__portes

    def informationsVehicule(self):
        print(f'La voiture de marque {self.get__marque()} est de modèle {self.get__modele()} sortit en {self.get__annee()} au prix de {self.get__prix()} € et à {self.__portes}')
    
    def demarrer(self):
        print(f'Faites chauffer la gomme')

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.__portes = portes
    
    def set__portes(self, portes):
        self.__portes = portes
    def get__portes(self):
        return self.__portes

    def informationsVehicule(self):
        print(f'La voiture de marque {self.get__marque()} est de modèle {self.get__modele()} sortit en {self.get__annee()} au prix de {self.get__prix()} € et à {self.__portes}')

    def demarrer(self):
        print(f'En Y sur le perif')

voiture = Voiture('Mercedes', 'Classe A', 2020, 18500)
voiture.informationsVehicule()
voiture.demarrer()
moto = Moto('Yamaha', '1200 Vmax', 1987, 4500)
moto.informationsVehicule()
moto.demarrer()