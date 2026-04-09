from abc import ABC, abstractmethod

# crearemos la clase abstracta
class Figura(ABC):
    @abstractmethod

    def calcular_area(self): # este metodo es obligatorio colocarlo en todos las subclases
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
        return ((self.lado ** 2) * 3.1416)

class Piramide(Figura):
     def __init__(self, base, altura):
          self.base = base
          self.altura = altura
     def calcular_area(self):
          return (self.base * self.altura) / 2


class Rectangulo(Figura):
     def __init__(self, base, altura):
          self.base = base
          self.altura = altura
     def calcular_area(self):
          return self.base * self.altura

class Cilindro(Figura):
     def __init__(self, radio, altura):
          self.radio = radio
          self.altura = altura
     def calcular_area(self):
          return 2 * 3.1416 * self.radio * self.altura

#vamos a ejecutar
def mostrar_area(figura: Figura):
     print(f"Area: {figura.calcular_area():.2f}")

def main():
     radio1 = float(input("ingrese el radio del circulo: "))
     circulo1 = Circulo(12)
     mostrar_area(circulo1)

     lado1 = float(input("ingrese el lado del cuadrado: "))
     cuadrado1 = Cuadrado(lado1)
     mostrar_area(cuadrado1)

     base2 = float(input("ingrese la base de la piramide: "))
     altura2 = float(input("ingrese la altura de la piramide: "))
     piramide1 = Piramide(base2, altura2)
     mostrar_area(piramide1)

     base3 = float(input("ingrese la base del rectangulo: "))
     altura3 = float(input("ingrese la altura del rectangulo: "))
     rectangulo1 = Rectangulo(base3, altura3)
     mostrar_area(rectangulo1)

     radio4 = float(input("ingrese el radio del cilindro: "))
     altura4 = float(input("ingrese la altura del cilindro: "))
     cilindro1 = Cilindro(radio4, altura4)
     mostrar_area(cilindro1)

if __name__ == "__main__":
    main()