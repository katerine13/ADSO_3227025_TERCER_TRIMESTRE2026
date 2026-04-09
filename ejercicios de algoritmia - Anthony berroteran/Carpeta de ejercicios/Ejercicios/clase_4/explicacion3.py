from abc import ABC, abstractmethod
from typing import List

#=========================================
# CLASE ABSTRACTA DE PERRO
#=========================================

class Perro(ABC):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres válida")
        
    @abstractmethod
    def raza(self) -> None:
        pass


#=========================================
# CLASES HIJAS
#=========================================

class Husky(Perro):
    def raza(self) -> None:
        print(f"{self.nombre} es un Husky Siberiano")


class PastorAleman(Perro):
    def raza(self) -> None:
        print(f"{self.nombre} es un Pastor Alemán")


class Pug(Perro):
    def raza(self) -> None:
        print(f"{self.nombre} es un Pug")


class Pitbull(Perro):
    def raza(self) -> None:
        print(f"{self.nombre} es un Pitbull")


#=========================================
# FUNCION
#=========================================

def hacer_sonido(perro: Perro) -> None:
    perro.raza()


#=========================================
# MAIN
#=========================================

def main() -> None:

    try:
        razas: List[Perro] = [
            Husky("Yako"),     #0
            PastorAleman("Goku"),  #1
            Pug("Canela"),     #2
            Pitbull("Andres")  #3
        ]

        print("Mostrar razas de los perros")
        for perro in razas:
            hacer_sonido(perro)

        # actualizar el nombre
        print("\nActualizar el nombre del Huski")
        razas[3].nombre = "Yakoso"
        print(f"El nombre es: {razas[3].nombre}")

        print("\nActualizar el nombre del PastorAleman")
        razas[3].nombre = "Camara"
        print(f"El nombre es: {razas[3].nombre}")

        print("\nActualizar el nombre del pug")
        razas[3].nombre = "Pulgas"
        print(f"El nombre es: {razas[3].nombre}")

        print("\nActualizar el nombre del Pitbull")
        razas[3].nombre = "Diablo"
        print(f"El nombre es: {razas[3].nombre}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()