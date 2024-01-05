import random

class Personnage:
    def __init__(self, name, life_points, armor, attack_name, attack_power):
        self.__name = name
        self.__life_points = life_points
        self.__armor = armor
        self.__attack_name = attack_name
        self.__attack_power = attack_power
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_life_points(self):
        return self.__life_points
    def set_life_points(self, life_points):
        self.__life_points = life_points
    def get_armor(self):
        return self.__armor
    def set_armor(self, armor):
        self.__armor = armor
    def get_attack_name(self):
        return self.__attack_name
    def set_attack_name(self, attack_name):
        self.__attack_name = attack_name
    def get_attack_power(self):
        return self.__attack_power
    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power
    def launch_attack(self, target):
        selected_attack = random.choice(self.get_attack_name())
        # print(self.get_attack_name())
        if selected_attack == "coup de poing":
            print(f"{self.__name} donne un coup de poing à {target.get_name()}")
            self.set_attack_power(random.randint(0, self.get_attack_power()))
            target.set_armor(random.randint(0, target.get_armor()))
            if self.__attack_power > target.get_armor():
                damage = self.__attack_power - target.get_armor()
                target.set_life_points(target.get_life_points() - damage)
                print(f"L'attaque {selected_attack} de {self.__name} inflige {damage} points de dégâts à {target.get_name()}")
                print(f"{target.get_name()} a maintenant {target.get_life_points()} points de vie")
            else:
                print(f"L'attaque {selected_attack} de {self.__name} n'inflige aucun dégât à {target.get_name()}")
        elif selected_attack == "soin":
            self.set_attack_power(random.randint(0, self.get_attack_power()))
            if self.__life_points < 100:
                print(f"{self.__name} se soigne de {self.__attack_power} points de vie")
                self.__life_points += self.__attack_power
                print(f"{self.__name} a maintenant {self.__life_points} points de vie")
            else:
                print(f"{self.__name} a déjà tous ses points de vie")

class Jeu:
    def level_difficulty(self):
        niveau = input("Choisissez un niveau de difficulté (facile, moyen, difficile) : ")
        while True:
            if niveau == "facile":
                return 1
            elif niveau == "moyen":
                return 2
            elif niveau == "difficile":
                return 3
            else:
                niveau = input("Choisissez un niveau de difficulté (facile, moyen, difficile) : ")
    def launch_game(self, niveau, personnage1, personnage2):
        if niveau == 1:
            personnage1.set_name("Guerrier")
            personnage1.set_life_points(200)
            personnage1.set_armor(5)
            personnage1.set_attack_name(["coup de poing", "soin"])
            personnage1.set_attack_power(20)
            personnage2.set_name("Gobelin")
            personnage2.set_life_points(20)
            personnage2.set_armor(0)
            personnage2.set_attack_name(["coup de poing"])
            personnage2.set_attack_power(10)
        elif niveau == 2:
            personnage1.set_name("Guerrier")
            personnage1.set_life_points(200)
            personnage1.set_armor(5)
            personnage1.set_attack_name(["coup de poing", "soin"])
            personnage1.set_attack_power(20)
            personnage2.set_name("Orc")
            personnage2.set_life_points(200)
            personnage2.set_armor(5)
            personnage2.set_attack_name(["coup de poing", "soin"])
            personnage2.set_attack_power(20)   
        elif niveau == 3:
            personnage1.set_name("Guerrier")
            personnage1.set_life_points(100)
            personnage1.set_armor(0)
            personnage1.set_attack_name(["coup de poing"])
            personnage1.set_attack_power(10)
            personnage2.set_name("Dragon")
            personnage2.set_life_points(200)
            personnage2.set_armor(10)
            personnage2.set_attack_name(["coup de poing", "soin"])
            personnage2.set_attack_power(20)

    def game_over(self, personnage1, personnage2):
        if personnage1.get_life_points() <= 0:
            return True
        elif personnage2.get_life_points() <= 0:
            return True
        else:
            return False


personnage1 = Personnage("", 0, 0, [], 0)
personnage2 = Personnage("", 0, 0, [], 0)
level1 = Jeu()
niveau = level1.level_difficulty()
level1.launch_game(niveau, personnage1, personnage2)

# personnage1.launch_attack(personnage2)
# # print(niveau)
# personnage2.launch_attack(personnage1)
# # print(niveau)
# personnage1.launch_attack(personnage2)
# # print(niveau)
# personnage2.launch_attack(personnage1)
# personnage1.launch_attack(personnage2)

while True:
    personnage1.launch_attack(personnage2)
    if level1.game_over(personnage1, personnage2):
        print(f"{personnage2.get_name()} est mort")
        break
    personnage2.launch_attack(personnage1)
    if level1.game_over(personnage1, personnage2):
        print(f"{personnage1.get_name()} est mort")
        break