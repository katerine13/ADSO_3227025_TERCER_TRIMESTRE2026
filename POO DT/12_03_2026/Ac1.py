from abc import ABC, abstractmethod
# Crearemos la clase abstracta

class Figura(ABC):
    @abstractmethod
    
    def calcular_area(self):  # Este metodo es obligatorio colocarlo en todas las subclases
        pass
    
# Ahora crearemos las clases hojas de figura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return ((self.radio ** 2) * 3.1416)
    
    
class Cuadrado(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular_area(self):
        return (self.lado1 * self.lado2)
    def calcular_area(self):
        pass
        
class Piramide(Figura):
    pass


class Rectangulo(Figura):
    pass


class Cilindro(Figura):
    pass


# Vamos a ejecutar

# Circulo
    
def mostrar_area(figura: Figura):
    print(f"Area: {figura.calcular_area():.2f}")
def main():
    radio1 = float(input("Ingrese el radio del circulo:  "))
    circulo1 = Circulo(radio1)
    mostrar_area(circulo1)

if __name__ == "__main__":
    main()
    
# Cuadrado

    lado1 = float(input("Ingrese el primer valor del cuadrado"))
    lado2 = float(input("Ingrese el segundo valor del cuadrado"))
    cuadrado1 = Cuadrado(lado1, lado2)
    mostrar_area(cuadrado1)