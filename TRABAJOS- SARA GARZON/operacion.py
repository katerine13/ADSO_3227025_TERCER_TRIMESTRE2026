from abc import ABC, abstractmethod
from typing import Optional

# 1 Interfaz
class Movible(ABC):
    # REPRESENTA animales que pueden desplazarse por si solos
    @abstractmethod
    def mover(self) -> None:
        pass 
class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre: str = "" #Privado y encapsulado
        self.nombre = nombre # YA nombre puedo utilizarlo (getter, setter)
    #Getter - MOSTRAR 
    @property
    def nombre(self) -> None: #Permite leer o mostar del animal de forma segura--
        return self._nombre
    
    #SETTER - Modifica la instancia del atributo en este caso el  nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() and nuevo_nombre != "":
         self._nombre = nuevo_nombre.strip().title()
        else:
            raise ValueError("El nombre ingresado debe ser una cadena de texto valida")
    @abstractmethod
    def sonido(self) -> None:
        pass
# crearemos Clases hijas para las dos ABC 
class Perro(Animal,Movible):
     def sonido(self) -> None:
         print(f"(self.nombre) El perro hace Guauu Guau")
class Vaca(Animal,Movible):
     def sonido(self) -> None:
         print(f"(self.nombre) El perro hace Guauu Guau")
class Vaca(Animal,Movible):
    def sonido(self) -> None:
        print(f"(self.nombre) La vaca hace Muuu MUUUUUUUU sigilosamente por mi casa")
class Elefante(Animal, Movible):
     def sonido(self) -> None:
         print(f"(self.nombre) brrrrr brrr ")
class Leon(Animal, Movible): 
     def mover(self) -> None:
         print(f"(self.nombre)El Leon se mueve sigilosamente por el SENA")      
#Realizaremos las funciones polimorfismo al rojo vivo
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()
    
def desplazar(animal:Movible) -> None:
    animal.mover()

def main():
    try:
        animales = {
            Perro("Rocky")
         
    }

#Actualizacion del nombre 
        print("Actualizacion del nombre")
        animales[3].nombre = "Mufaza"
        print(f"El nuevo nombre es : {animales[3].nombre}")   
    except ValueError as e:
        print(f"Eror,{e}")

if __name__ == "_main_":
    main()
