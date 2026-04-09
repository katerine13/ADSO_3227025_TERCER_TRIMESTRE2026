from abc import ABC, abstractmethod

from typing import Optional

# 1 intefaz
class Movible(ABC):
    # representa animales que pueden desplazarse por si solos
    @abstractmethod
    def mover(self) -> None:
        pass

class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = "" # privado y encapsulado
        self.nombre = nombre #ya nombre puedo utilizalo nombre (getter, setter)
    # GETTER - MOSTRAR
    @property
    def nombre(self) -> None: # permite leer o mostrar el nombre del animal de forma segura
        return self.__nombre
    
    # SETTER - modifica la instancia del atributo en este caso nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() and nuevo_nombre != "":
            self.__nombre = nuevo_nombre.strip().title()
    @abstractmethod
    def sonido(self) -> None:
        pass


# crearemos class hijas para las dos ABC
class Perro(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} el perro hace Guauu")

class Gato(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} el gato hace Miau")

class Vaca(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} la vaca hace Muuu")

#  crearemos clases hijas de las dos clases ABC
class Leon(Animal, Movible):
    def sonido(self) -> None:
        print(f"{self.nombre} El leon hace: Roooar")

    def mover(self) -> None:
        print(f"{self.nombre} El Leon se mueve sigilosamente por el SENA")

# realizar los funcionaminetos polimorfismo al rojo vivo
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()

def desplazar(animal: Animal) -> None:
    animal.mover()

def main() -> None:

    try:
        animales = [
            Perro("Rocky"), #0
            Gato("Misu"), #1
            Vaca("Lola"), #2
            Leon("Simba") #3
        ]
        print("========== POLIMORFISMO EN NUESTRO ZOOLOGICO ==========")
        for animal in animales:
            hacer_sonido(animal)

        print("animales con movimiento")
        for animal in animales:
            if isinstance(animal, Movible):
                desplazar(animal)
# actualizar del nimbre
        print("actualizar el nombre")
        animales[3].nombre = "Mufasa"
        print(f"el nombre es: {animales[3].nombre}")

    except ValueError as e:
        print(f"Error, {e}")


if __name__ == "__main__":
    main()