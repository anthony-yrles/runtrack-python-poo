import random

class Carte:
    def __init__(self):
        self.__valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.__couleur = ['Heart', 'Spades', 'Diamonds', 'Clubs']

    def set_valeur(self, valeur):
        self.__valeur = valeur
    
    def get_valeur(self):
        return self.__valeur
    
    def set_couleur(self, couleur):
        self.__couleur = couleur
    
    def get_couleur(self):
        return self.__couleur
        
    def valeur_return(self, valeur_carte):
        if isinstance(valeur_carte, int):
            return valeur_carte
        elif valeur_carte in ['J', 'Q', 'K']:
            return 10
        elif valeur_carte == 'A':
            choix = input('1 ou 11? ')
            while choix not in ['1', '11']:
                choix = input('Veuillez choisir 1 ou 11: ')
            return int(choix)
        else:
            print('Valeur de carte non reconnue. Utilisation de la valeur par défaut (1).')
            return 1


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
    
    def distribuer(self):
        joueurs = [[] for _ in range(2)]

        for _ in range(2):
            for i in range(2):
                carte = random.choice(self.get_paquet())
                joueurs[i].append(carte)
                self.retirer_du_paquet(carte)

        return joueurs
    
    def draw_a_card(self, joueur_main):
        carte = random.choice(self.get_paquet())
        joueur_main.append(carte)
        self.retirer_du_paquet(carte)

    def test_jeu(self, list_mains):
        jeu_en_cours = True
        player_total = 0
        total_croupier = 0
        if jeu_en_cours:
            for main in list_mains:
                if main != list_mains[-1] and jeu_en_cours:
                    total = 0
                    for carte in main:
                        valeur_carte = Carte().valeur_return(carte[1])
                        total += valeur_carte
                    print(f"Votre total: {total}")

                    while total < 21:
                        choice = input(f"Voulez-vous: prendre ou passer ? ")

                        if choice == 'prendre':
                            self.draw_a_card(main)
                            nouvelle_carte = main[-1]
                            nouvelle_valeur = Carte().valeur_return(nouvelle_carte[1])
                            total += nouvelle_valeur
                            print(f'Vous tirez la carte {nouvelle_carte}')
                            print(f"Votre total: {total}")

                            if total == 21:
                                print(f"Félicitations, vous avez atteint le score de 21. Black Jack!")
                                jeu_en_cours = False
                                break

                            elif total > 21:
                                print(f'Bouhouhouhou, vous avez dépassé 21. Vous avez perdu.')
                                jeu_en_cours = False
                                break

                        elif choice == 'passer':
                            print(f'Vous passez avec {total} points, au tour du joueur suivant')
                            player_total = total
                            break

                else:
                    total = 0
                    for carte in main:
                        valeur_carte = Carte().valeur_return(carte[1])
                        total += valeur_carte

                    print(f"Total croupier: {total}")

                    while total < 17:
                        self.draw_a_card(list_mains)
                        nouvelle_carte = main[-1]
                        print(f'le croupier tire la carte {nouvelle_carte}')
                        nouvelle_valeur = Carte().valeur_return(nouvelle_carte[1])
                        total += nouvelle_valeur
                        print(f"Total croupier: {total}")

                    print(f'Le croupier a maintenant {total} points.')

                    if 17 <= total <= 21:
                        total_croupier = total
                        print(f"Le croupier s'arrete avec {total_croupier} points")
                        jeu_en_cours = False

                    if total > 21:
                        print(f'Le croupier à dépasser les 21, vous avez gagné!')
                        jeu_en_cours = False

            return player_total, total_croupier

    def test_victoire(self, player_total, total_croupier):
        if player_total > total_croupier:
            print('Bravo vous avez gagné')
        else:
            print(f'Le croupier avec {total_croupier} est le plus propre de 21 vous avez perdu')

jeu = Jeu()
main_des_joueurs = jeu.distribuer()
total = jeu.test_jeu(main_des_joueurs)
player_total, total_croupier = total
jeu.test_victoire(player_total, total_croupier)