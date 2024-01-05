import random

class Carte:
    def __init__(self):
        self.__valeur = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.__couleur = ['Heart', 'Spades', 'Diamonds', 'Clubs']

    def set_valeur(self, valeur):
        self.__valeur = valeur
    
    def get_valeur(self):
        return self.__valeur
    
    def set_couleur(self, couleur):
        self.__couleur = couleur
    
    def get_couleur(self):
        return self.__couleur
    
    def valeur_return(self):
        if self.__valeur >= 2 and self.__valeur <= 10:
            return self.__valeur
        elif self.__valeur == 'J' or self.__valeur == 'Q' or self.__valeur == 'K':
            return 10
        elif self.__valeur == 1:
            choix = input('1 ou 11? ')
            while choix not in ['1', '11']:
                choix = input('Veuillez choisir 1 ou 11: ')
            return int(choix)

class Jeu(Carte):
    def __init__(self):
        Carte.__init__(self)
        self.__paquet = [(i, j) for i in self.get_couleur() for j in self.get_valeur()]

    def set_paquet(self, paquet):
        self.__paquet = paquet
    
    def get_paquet(self):
        return self.__paquet
    
    def retirer_du_paquet(self, carte):
        self.__paquet.remove(carte)
    
    def distribuer(self, nombre_joueurs):
        joueurs = [[] for _ in range(nombre_joueurs)]

        for _ in range(2):
            for i in range(nombre_joueurs):
                carte = random.choice(self.get_paquet())
                joueurs[i].append(carte)
                self.retirer_du_paquet(carte)

        return joueurs
    
    def draw_a_card(self, joueurs, i):
        carte = random.choice(self.get_paquet())
        joueurs[i].append(carte)
        self.retirer_du_paquet(carte)
        Carte.set_valeur(carte[1])
    
    def test_jeu(self, list_mains):
        for i in list_mains:
            if i != list_mains[0]:
                for j in range(2):
                    total = Carte.valeur_return(list_mains[i][j][Carte.get_valeur()]) + Carte.valeur_return(list_mains[i][j][Carte.get_valeur()])
                    print(total)
                    choice = input(['prendre', 'passer'])
                    while choice not in ['prendre', 'passer']:
                        choice = input(['prendre', 'passer'])
                        while choice not in('passer'):
                            self.draw_a_card(list_mains, i)
                            total = total + Carte.valeur_return(list_mains[i])
                            if total == 21:
                                total_joueur = total
                                print(f"Féliciation vous avez atteint le score de {total} vous avez gagné")
                                return total_joueur
                            elif total > 21:
                                total_joueur = total
                                print(f'Bouhouhouhou vous avez dépassé {total} vous avez perdu')
                                return total_joueur
                        print(f'Vous passez avec {total} points, au tour du joueur suivant')
            else:
                for j in range(2):
                    total = Carte.valeur_return(list_mains[i][j][Carte.get_valeur()]) + Carte.valeur_return(list_mains[i][j][Carte.get_valeur()])
                    if total < 17:
                        self.draw_a_card(list_mains, 0)
                        total = total + Carte.valeur_return(list_mains[i])
                    elif total >= 17 and total <= 21:
                        total_croupier = total
                        return total_croupier

jeu = Jeu()
main_des_joueurs = jeu.distribuer(4)
print(main_des_joueurs)
jeu.test_jeu(main_des_joueurs)