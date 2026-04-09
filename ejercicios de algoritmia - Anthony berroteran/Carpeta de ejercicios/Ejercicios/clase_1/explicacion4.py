class Mueble:
    def __init__(self, nombre, material, precio):
        self.nombre = nombre
        self.material = material
        self.precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: Debe ingresar un nombre válido.")

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, nuevo_material):
        if isinstance(nuevo_material, str) and len(nuevo_material) > 0:
            self.__material = nuevo_material
        else:
            print("Error: Debe ingresar un material válido.")

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: Debe ingresar un precio válido.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Material: {self.material}")
        print(f"Precio: ${self.precio}\n")


class Mochila:
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and len(nueva_marca) > 0:
            self.__marca = nueva_marca
        else:
            print("Error: Debe ingresar una marca válida.")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, nuevo_color):
        if isinstance(nuevo_color, str) and len(nuevo_color) > 0:
            self.__color = nuevo_color
        else:
            print("Error: Debe ingresar un color válido.")

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        if isinstance(nueva_capacidad, (int, float)) and nueva_capacidad > 0:
            self.__capacidad = nueva_capacidad
        else:
            print("Error: Debe ingresar una capacidad válida.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad} litros\n")



def main():
    print("=== Bienvenido al programa ===\n")

    # ----- MUEBLE -----
    mueble1 = Mueble("Silla", "Madera", 15000)
    print("Información del mueble:")
    mueble1.mostrar_info()

    nuevo_precio = float(input("Ingrese el nuevo precio para la silla: "))
    mueble1.precio = nuevo_precio

    nuevo_nombre = input("Ingrese el nuevo nombre para la silla: ")
    mueble1.nombre = nuevo_nombre

    print("\nInformación actualizada del mueble:")
    mueble1.mostrar_info()

    mochila1 = Mochila("Nike", "Negra", 20)
    print("Información de la mochila:")
    mochila1.mostrar_info()

    nueva_capacidad = float(input("Ingrese la nueva capacidad para la mochila: "))
    mochila1.capacidad = nueva_capacidad

    nuevo_color = input("Ingrese el nuevo color para la mochila: ")
    mochila1.color = nuevo_color

    print("\nInformación actualizada de la mochila:")
    mochila1.mostrar_info()


if __name__ == "__main__":
    main() 