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
        print('Bonjour')

    def modifierAge(self, new_age):
        self._age = new_age

class Eleve(Personne):
    def __init__(self, age=14):
        Personne.__init__(self, age)
    def allerEnCours(self):
        print('Je vais en cours')
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
        
eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.afficherAge()
professeur = Professeur(40, 'Géometrie')
professeur.bonjour()
professeur.enseigner()