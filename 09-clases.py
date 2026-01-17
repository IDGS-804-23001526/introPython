"""
    Una clase es un molde para crear objetos 
    self : es una referencia a la instancia actual de la clase this
"""

class OperasBas:
    # Declaracion de propiedades
    num1 = 0
    num2 = 0
    res = 0

    # Declaracion del constructor this
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    # Declaracion de metodos de clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))
    
    def resta(self):
        self.res = self.num1 - self.num2
        print("La resta es: {}".format(self.res))

def main():
    obj = OperasBas();
    obj.suma()
    obj.resta()

if __name__ == "__main__":
    main()