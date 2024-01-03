class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def set__marque(self, marque):
        self.__marque = marque

    def set__modele(self, modele):
        self.__modele = modele

    def set__annee(self, annee):
        self.__annee = annee

    def set__kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set__en_marche(self, en_marche):
        if not en_marche:
            self.__en_marche = True
        else:
            self.__en_marche = False
    
    def set__reservoir(self, reservoir):
        self.__reservoir = reservoir
    
    def get__marque(self):
        return self.__marque
    
    def get__modele(self):
        return self.__modele
    
    def get__annee(self):
        return self.__annee
    
    def get__kilometrage(self):
        return self.__kilometrage
    
    def get__en_marche(self):
        return self.__en_marche

    def get__reservoir(self):
        return self.__reservoir
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            if self.get__en_marche() == True:
                self.set__en_marche(self.get__en_marche())
                print('La voiture demarre')
            else:
                print("Demarrer la voitude s'il vous plais")
        else:
            print("Mettre de l'essance")
    
    def arreter(self):
        if self.get__en_marche() == True:
            self.set__en_marche(self.get__en_marche())

    def __verifier_plein(self):
        return self.get__reservoir()

voiture = Voiture('','',0,0)
voiture.set__en_marche(True)
voiture.demarrer()
voiture.set__en_marche(False)
voiture.demarrer()
voiture.set__reservoir(4)
voiture.demarrer()
