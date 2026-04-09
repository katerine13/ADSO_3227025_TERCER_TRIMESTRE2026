from abc import ABC, abstractmethod

#  CON MODIFICADORES DE ACCESO

class Animal(ABC):

    def __init__(self, nombre, edad):
        self.nombre   = nombre
        self._edad    = edad
        self.__energia = 100 

    # Getter: forma segura de leer __energia
    def get_energia(self):
        return self.__energia

    # Setter: valida antes de cambiar __energia
    def set_energia(self, valor):
        if 0 <= valor <= 100:
            self.__energia = valor
        else:
            print("Error: la energía debe estar entre 0 y 100")

    # Método abstracto: las clases hijas DEBEN implementarlo
    @abstractmethod
    def hablar(self):
        pass


# Herencia: Perro hereda de Animal
class Perro(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # Polimorfismo: cada animal implementa hablar() a su manera
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"


# Herencia: Gato hereda de Animal
class Gato(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # Polimorfismo
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"





#  SIN MODIFICADORES DE ACCESO

class AnimalSimple:

    def __init__(self, nombre, edad):
        self.nombre  = nombre 
        self.edad    = edad
        self.energia = 100

    def hablar(self):
        return f"{self.nombre} hace un sonido"


class PerroSimple(AnimalSimple):

    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"


class GatoSimple(AnimalSimple):

    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"


def main():

    # Prueba CON modificadores 
    print("=== CON MODIFICADORES ===")

    perro = Perro("Max", 3)
    gato  = Gato("Luna", 2)

    # Polimorfismo: misma llamada, resultado diferente
    for animal in [perro, gato]:
        print(animal.hablar())

    # Encapsulamiento: acceso controlado
    print(perro.get_energia())       # 100
    perro.set_energia(80)
    print(perro.get_energia())       # 80
    perro.set_energia(200)           # Error: valor inválido

    # Atributo privado: no se puede acceder directo
    try:
        print(perro.__energia)
    except AttributeError:
        print("No se puede acceder a __energia directamente")

    # Abstracción: no se puede crear un Animal directamente
    try:
        a = Animal("X", 1)
    except TypeError:
        print("No se puede crear un Animal, es abstracto")

    # Prueba SIN modificadores
    print("\n=== SIN MODIFICADORES ===")

    perro2 = PerroSimple("Rex", 3)
    gato2  = GatoSimple("Misi", 2)

    # Polimorfismo: también funciona
    for animal in [perro2, gato2]:
        print(animal.hablar())

    # Sin control: cualquier valor se acepta
    perro2.energia = 999   # no hay validación
    perro2.edad    = -5    # tampoco
    print(f"Energía: {perro2.energia}")  # 999 ← peligroso
    print(f"Edad: {perro2.edad}")        # -5  ← peligroso

    # Sin abstracción: se puede crear la clase base directamente
    base = AnimalSimple("Genérico", 0)
    print(base.hablar())   # funciona aunque no tiene sentido


if __name__ == "__main__":
    main()