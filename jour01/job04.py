class Personne:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
    def SePresenter(self, nom, prenom):
        return(nom, prenom)
    
presentation = Personne()
presentation.nom = input()
presentation.prenom = input()
presentation.SePresenter(presentation.nom, presentation.prenom)
print(f"Mon nom est {presentation.nom} {presentation.prenom}")



