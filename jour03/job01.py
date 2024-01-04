class Ville:
    def __init__(self, city_name, habitant_number):
        self.__city_name = city_name
        self.__habitant_number = habitant_number
    def set__nom(self, city_name):
        self.__city_name = city_name
    def set__habitant_number(self, habitant_number):
        self.__habitant_number = habitant_number
    def get__city_name(self):
        return self.__city_name
    def get__habitant_number(self):
        return self.__habitant_number

class Personne:
    def __init__(self, person_name, age, class_ville_object):
        self.__person_name = person_name
        self.__age = age
        self.__class_ville_object = class_ville_object
    def set__person_name(self, person_name):
        self.__person_name = person_name
    def set__age(self, age):
        self.__age = age
    def set__class_ville_object(self, class_ville_object):
        self.__class_ville_object = class_ville_object
    def get__person_name(self):
        return self.__person_name
    def get__age(self):
        return self.__age
    def get__class_ville_object(self):
        return self.__class_ville_object
    def add_habitant(self, class_ville_object):
        class_ville_object.set__habitant_number(class_ville_object.get__habitant_number()+1)
        print(f'Mise à jour de la population de la ville de {class_ville_object.get__city_name()} {class_ville_object.get__habitant_number()} habitants')
        
    
paris = Ville('Paris', 1000000)
print(f"Le nombre d'habitants de la ville de {paris.get__city_name()} est {paris.get__habitant_number()}")
marseille = Ville('Marseille', 861635)
print(f"Le nombre d'habitants de la ville de {marseille.get__city_name()} est {marseille.get__habitant_number()}")

john = Personne('John', '45', paris)
print(f"{john.get__person_name()} arrive à {paris.get__city_name()} à l'age de {john.get__age()} ans")

myrtille = Personne('Myrtille', '4', paris)
print(f"{myrtille.get__person_name()} arrive à {paris.get__city_name()} à l'age de {myrtille.get__age()} ans")

chloe = Personne('Chloe', '18', marseille)
print(f"{chloe.get__person_name()} arrive à {marseille.get__city_name()} à l'age de {chloe.get__age()} ans")

john.add_habitant(john.get__class_ville_object())
myrtille.add_habitant(myrtille.get__class_ville_object())
chloe.add_habitant(chloe.get__class_ville_object())