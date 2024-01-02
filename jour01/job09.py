class Produit:
    def __init__(self):
        self.nom = ""
        self.prixHT = 500
        self.TVA = 10
    def CalculerPrixTTC(self):
        result = float(self.prixHT) + float(self.prixHT) * float(self.TVA) / 100
        return result
    def afficher(self):
        affichage = f"Le nom du produit est {self.modifyName()}, son prix HT est {self.modifyPrix()} €, la TVA est de {self.modifyTVA()} %, le prix TTC est {self.CalculerPrixTTC()} €"
        return affichage
    def modifyName(self):
        self.nom = input()
        return self.nom
    def modifyPrix(self):
        self.prixHT = input()
        return self.prixHT
    def modifyTVA(self):
        self.TVA = input()
        return self.TVA


    
produit = Produit()
# produit.modifyName()
# produit.modifyPrix()
# produit.modifyTVA()
# produit.CalculerPrixTTC()
affichage = produit.afficher()
print(affichage)


