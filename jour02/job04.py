class Student:
    def __init__(self, name, last_name, etudiant_number, number_of_credit=0):
        self.__name = name
        self.__last_name = last_name
        self.__etudiant_number = etudiant_number
        self.__number_of_credit = number_of_credit
        self.__level = self._Student__studentEval()
    def set__name(self, name):
        self.__name = name
    def set__last_name(self, last_name):
        self.__last_name = last_name
    def set__etudiant_number(self, etudiant_number):
        self.__etudiant_number = etudiant_number
    def set__number_of_credit(self, number_of_credit):
        self.__number_of_credit = number_of_credit
    def set__level(self, level):
        self.__level = level
    def get__name(self):
        return self.__name
    def get__last_name(self):
        return self.__last_name
    def get__etudiant_number(self):
        return self.__etudiant_number
    def get__number_of_credit(self):
        return self.__number_of_credit
    def get__level(self):
        return self.__level
    def add_credit(self, number_of_credit):
        if number_of_credit > 0:
            self.__number_of_credit = self.get__number_of_credit() + number_of_credit
    def __studentEval(self):
        if self.get__number_of_credit() >= 90:
            self.set__level('Excellent')
        elif self.get__number_of_credit() >= 80:
            self.set__level('Tres bien')
        elif self.get__number_of_credit() >= 70:
            self.set__level('Bien')
        elif self.get__number_of_credit() >= 60:
            self.set__level('Passable')
        elif self.get__number_of_credit() < 60:
            self.set__level('Insuffisant')
    def studentInfo(self):
        print(f"L'etudiant n° {str(student.get__etudiant_number())} nommé {student.get__last_name()} {student.get__name()} est d'un level {student.get__level()} ")


student = Student('Doe', 'John', 145)
print(f"L'etudiant n° {str(student.get__etudiant_number())} nommé {student.get__last_name()} {student.get__name()} possede {str(student.get__number_of_credit())} ")
student.add_credit(30)
student.add_credit(30)
student.add_credit(20)
print(f"L'etudiant n° {str(student.get__etudiant_number())} nommé {student.get__last_name()} {student.get__name()} possede {str(student.get__number_of_credit())} ")
print(student._Student__studentEval())
student.studentInfo()