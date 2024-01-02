class Operation:
    def addition(self, nombre1, nombre2):
        self.nombre1 = self.nombre1 + nombre1
        self.nombre2 = self.nombre2 + nombre2
        print(self.nombre1 + self.nombre2)

result = Operation()
result.addition(12, 3)