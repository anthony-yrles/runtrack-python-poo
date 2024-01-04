class Joueur:
    def __init__(self, name, number, position, goal_scored, decisive_pass, yellow_card, red_card):
        self.__name = name
        self.__number = number
        self.__position = position
        self.__goal_scored = goal_scored
        self.__decisive_pass = decisive_pass
        self.__yellow_card = yellow_card
        self.__red_card = red_card

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def set_goal_scored(self, goal_scored):
        self.__goal_scored = goal_scored

    def get_goal_scored(self):
        return self.__goal_scored

    def set_decisive_pass(self, decisive_pass):
        self.__decisive_pass = decisive_pass

    def get_decisive_pass(self):
        return self.__decisive_pass

    def set_yellow_card(self, yellow_card):
        self.__yellow_card = yellow_card

    def get_yellow_card(self):
        return self.__yellow_card

    def set_red_card(self, red_card):
        self.__red_card = red_card

    def get_red_card(self):
        return self.__red_card

    def score_a_goal(self):
        self.set_goal_scored(self.get_goal_scored() + 1)

    def decisive_passe_done(self):
        self.set_desicive_pass(self.get_desicive_pass() + 1)

    def yellow_card_recived(self):
        self.set_yellow_card(self.get_yellow_card() + 1)

    def red_card_recived(self):
        self.set_red_card(self.get_red_card() + 1)

    def show_stats(self):
        return f'Le joueur {self.get_name()} numéro {self.get_number()} qui joue {self.get_position()} a marqué {self.get_goal_scored()} buts et données {self.get_decisive_pass()} il a reçu {self.get_yellow_card()} cartons jaunes et {self.get_red_card()} cartons rouges'

class Equipe:
    def __init__(self, team_name, player_list):
        self.__team_name = team_name
        self.__player_list = player_list

    def set_team_name(self, team_name):
        self.__team_name = team_name

    def get_team_name(self):
        return self.__team_name

    def set_player_list(self, player_list):
        self.__player_list = player_list

    def get_player_list(self):
        return self.__player_list

    def add_player(self, player):
        self.__player_list.append(player)
    
    def show_player_stats(self):
        for player in self.__player_list:
            print(player.show_stats())
    
    def change_stats(self, player, number, position, goal_score, decisive_pass, yellow_card, red_card):
        player.set_number(number)
        player.set_position(position)
        player.set_goal_scored(goal_score)
        player.set_decisive_pass(decisive_pass)
        player.set_yellow_card(yellow_card)
        player.set_red_card(red_card)

joueur1 = Joueur("Lionel Messi", 10, "Attaquant", 30, 15, 2, 0)
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant", 28, 10, 1, 0)
joueur3 = Joueur("Pierre-Aymeric Aubameyang", 11, "Ailier", 15, 8, 3, 1)
joueur4 = Joueur("Kevin De Bruyne", 17, "Milieu de terrain", 10, 20, 4, 0)
joueur5 = Joueur("Virgil van Dijk", 4, "Défenseur central", 5, 2, 1, 0)

equipe = Equipe('Olympique de marseille', [])
equipe.add_player(joueur1)
equipe.add_player(joueur2)
equipe.add_player(joueur3)
equipe.add_player(joueur4)
equipe.add_player(joueur5)
equipe.show_player_stats()
equipe.change_stats(joueur1, 1, "Milieu", 35, 18, 3, 1)
print(joueur1.show_stats())
joueur2.yellow_card_recived()
joueur3.score_a_goal()
joueur1.red_card_recived()
joueur4.decisive_passe_done()
joueur5.yellow_card_recived()
equipe.show_player_stats()