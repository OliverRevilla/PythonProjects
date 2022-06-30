class Programas:
    def __init__(self,nombre,uso,descripcion):
        self.nombre = nombre
        self.uso = uso
        self.descripcion = descripcion

    def identity(self):
        print(self.nombre)

    def description(self):
        print(self.descripcion)

AMD = Programas("AMD","Debugging","Uso de compiladores")
AMD.description()




