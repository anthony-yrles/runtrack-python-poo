class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def veillir(self, age):
        age += 1
        return age
    def nommer(self, prenom):
        prenom = input()
        return(prenom)

testAge = Animal()
print(f"L'age de l'animal est {testAge.age}")
testAge.age = int(input())
print(f"L'age de l'animal est {testAge.veillir(testAge.age)}")
print(f"Le prenom de l'animal est {testAge.nommer(testAge.prenom)}")