class CompteBancaire:
    def __init__(self, account_number, last_name, first_name, account_balance, overdraft: bool):
        self.__account_number = account_number
        self.__last_name = last_name
        self.__first_name = first_name
        self.__account_balance = account_balance
        self.__overdraft = overdraft
    def set__account_number(self, account_number):
        self.__account_number = account_number
    def set__last_name(self, last_name):
        self.__last_name = last_name
    def set__first_name(self, first_name):
        self.__first_name = first_name
    def set__account_balance(self, account_balance):
        self.__account_balance = account_balance
    def set__overdraft(self):
        if self.__overdraft:
            self.__overdraft = False
        else:
            self.__overdraft = True

    def get__account_number(self):
        return self.__account_number
    def get__last_name(self):
        return self.__last_name
    def get__first_name(self):
        return self.__first_name
    def get__account_balance(self):
        return self.__account_balance
    def get__overdraft(self):
        return self.__overdraft

    def afficher(self):
        print(f"Le compte numéro {self.get__account_number()} appartient à {self.get__last_name()} {self.get__first_name()} sont solde est de {self.get__account_balance()}")
    def afficherSolde(self):
        print(f"Le solde est de {self.get__account_balance()} €")
    def versement(self, amount_to_add):
        self.set__account_balance(self.get__account_balance() + amount_to_add)
    def retrait(self, amount_to_withdraw: int):
        if amount_to_withdraw > 0:
            if self.get__overdraft() == True:
                self.set__account_balance(self.get__account_balance() - amount_to_withdraw)
            elif self.get__overdraft == False and amount_to_withdraw < self.get__account_balance():
                self.set__account_balance(self.get__account_balance() - amount_to_withdraw)
            else:
                print("Vous ne possedez pas assez d'argent pour effectuer ce retrait")
        print("Veuillez selctionner un montant superieur a 0")
    def agios(self):
        if self.get__account_balance() < 0:
            self.set__account_balance(self.get__account_balance() - 8)
    def virement(self, reference, amount, compte_bancaire):
        if self.get__account_balance() > amount:
            compte_bancaire.set__account_balance(compte_bancaire.get__account_balance() + amount)
            self.set__account_balance(self.get__account_balance()- amount)
            print(f"Virement {reference} d'un montant de {amount} € effectué vers le compte numéro {compte_bancaire.get__account_number()} votre solde de compte est {self.get__account_balance()} €")
        elif self.get__account_balance < amount and self.get__overdraft() == True:
            self.set__account_balance(self.get__account_balance()- amount)
            self.agios()
            print(f"Virement {reference} d'un montant de {amount} € effectué vers le compte numéro {compte_bancaire.get__account_number()} votre solde de compte est {self.get__account_balance()} €")
        else:
            print(f"Virement {reference} d'un montant de {amount}")

compte1= CompteBancaire(1, 'Yrles', 'Anthony', 1000, True)
compte2= CompteBancaire(2, 'Serra', 'Matthis', -300, True)

compte2.afficher()
compte1.virement('Blop', 300, compte2)
compte2.afficher()


    


