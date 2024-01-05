class Personne:
    def __init__(self, age=14):
        self._age = age

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age
    
    def afficheAge(self):
        print(self._age)

    def bonjour(self):
        print('bonjour')

    def modifierAge(self, new_age):
        self._age = new_age

class Eleve(Personne):
    def __init__(self, age):
        Personne.__init__(self, age)
    def allerEnCours(self):
        print('Aller en cours')
    def afficherAge(self):
        print(f"J'ai {self.get_age()}")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        Personne.__init__(self, age)
        self.__matiereEnseignee = matiereEnseignee

    def set__matiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    def get__matiereEnseignee(self):
        return self.__matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
        


eleve = Eleve(14)
eleve.modifierAge(18)
eleve.afficherAge()