class Commande:
    
    def __init__(self, number_of_command, plate_commanded, status_command):
        self.__number_of_command = number_of_command
        self.__plate_commanded = plate_commanded
        self.__status_command = status_command
        self.menu = {'Plats1': ['ravioli', 15.4], 'Plats2': ['Tartiflette', 8.2], 'Plats3': ['Tajine', 15.4], 'Plats4': ['Lasagne', 12.3]}

    def set__number_of_command(self, number_of_command):
        self.__number_of_command = number_of_command

    def set__plate_commanded(self, plate_name, price):
        self.__plate_commanded[plate_name] = price

    def set__status_command(self, status_command):
        self.__status_command = status_command

    def get_number_of_command(self):
        return self.__number_of_command
    def get__plate_commanded(self):
        return self.__plate_commanded
    def get__status_command(self):
        if self.__status_command == 0:
            return 'Commande annulée'
        if self.__status_command == 1:
            return 'Commande en cours'
        if self.__status_command == 2:
            return 'Commande terminé'

    def add_plates(self, plate_name):
        if plate_name in self.menu:
            self.set__plate_commanded(plate_name, self.menu[plate_name][1])  # Assuming you want to store the price
        else:
            print(f"Plate '{plate_name}' not found in the menu.")

    def del_command(self):
        if self.get__status_command() == 1:
            self.set__status_command(0)
    
    def __total_command(self):
        total = 0
        for price in self.get__plate_commanded().values():
            total += price
        return total
    
    def total_TVA_incluse(self):
        total = self.__total_command() + self.__total_command() * 0.2
        return total
    
    def afficher_total(self):
        print(self.__total_command())
        print(self.total_TVA_incluse())

commande = Commande(1, {}, 1)
commande.add_plates('Plats1')
commande.add_plates('Plats4')
commande.afficher_total()
commande.add_plates('Plats1')
commande.add_plates('Plats2')
commande.afficher_total()