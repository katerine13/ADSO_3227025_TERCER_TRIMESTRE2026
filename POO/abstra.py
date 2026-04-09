from abc import ABC, abstractmethod

# creamos la clase abstracta

class Figura(ABC):
    @abstractmethod
    
    def calcular_area(self): # este metodo es obligatorio colocarlo en todas las subclases
        pass

# ahora crearemos las clases hijas de figura
class Circulo(Figura):
    
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return ((self.radio ** 2) * 3.1416)
    
class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return ((self.lado * 2))

class Piramide(Figura):

    def __init__(self, area_lateral, area_base):
        self.area_base = area_base
        self.area_lateral = area_lateral

    def calcular_area(self):
        return (self.area_base + self.area_lateral)       

class Rectangulo(Figura):
    
    def __init__(self, base, base2):
        self.base = base
        self.base2 = base2

    def calcular_area(self):
        return (self.base * self.base2)
    
class Cilindro(Figura):
    
    def __init__(self, area1, area2, area3):
        self.area1 = area1
        self.area2 = area2
        self.area3 = area3

    def calcular_area(self):
        return (self.area1 + self.area2 + self.area3)
    
# vamos a ejecutar la funcion

def mostrar_area(figura: Figura):
    print(f"Area: {figura.calcular_area():.2f}")

def main():
    num = int(input("ingrese un numero: "))
    circulo = Circulo(num)
    mostrar_area(circulo)

    num = int(input("ingrese un numero: "))
    cuadrado = Cuadrado(num)
    mostrar_area(cuadrado)

    area_base = int(input("ingrese un numero: "))
    area_lateral= int(input("ingrese un numero: "))
    piramide = Piramide(area_base, area_lateral)
    mostrar_area(piramide)

    base = int(input("ingrese un numero: "))
    base2 = int(input("ingrese un numero: "))
    rectangulo = Rectangulo(base, base2)
    mostrar_area(rectangulo)

    area1 = int(input("ingrese un numero: "))
    area2 = int(input("ingrese un numero: "))
    area3 = int(input("ingrese un numero: "))
    cilindro = Cilindro(area1, area2, area3)
    mostrar_area(cilindro)
if __name__ == "__main__":
    main()