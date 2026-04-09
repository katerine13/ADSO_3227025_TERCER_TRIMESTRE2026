class Mueble:
    def __init__(self, nombre, material, precio):
        self.__nombre = nombre
        self.__material = material
        self.__precio = precio

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_material(self):
        return self.__material

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: Debe ingresar un nombre válido.")

    def set_material(self, nuevo_material):
        if isinstance(nuevo_material, str) and len(nuevo_material) > 0:
            self.__material = nuevo_material
        else:
            print("Error: Debe ingresar un material válido.")

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: Debe ingresar un precio válido.")

    # Método para mostrar información del mueble
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Material: {self.__material}")
        print(f"Precio: ${self.__precio}\n")

def main():
    print("=== Bienvenido al programa de muebles ===\n")

    # Crear un objeto Mueble
    mueble1 = Mueble("Silla", "Madera", 15000)

    # Mostrar información del mueble
    print("Información del mueble:")
    mueble1.mostrar_info()

    # Actualizar el precio del mueble
    nuevo_precio = float(input("Ingrese el nuevo precio para la silla: "))
    mueble1.set_precio(nuevo_precio)

    # Mostrar la información actualizada del mueble
    print("\nInformación actualizada del mueble:")
    mueble1.mostrar_info()
    # Actualizar el nombre del mueble
    nuevo_nombre = input("Ingrese el nuevo nombre para la silla: ")
    mueble1.set_nombre(nuevo_nombre)
    # Mostrar la información actualizada del mueble
    print("\nInformación actualizada del mueble:")
    mueble1.mostrar_info()
if __name__ == "__main__":
    main()



class mochila:
    def __init__(self, marca, color, capacidad):
        self.__marca = marca
        self.__color = color
        self.__capacidad = capacidad

    # Getters
    def get_marca(self):
        return self.__marca

    def get_color(self):
        return self.__color

    def get_capacidad(self):
        return self.__capacidad

    # Setters
    def set_marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and len(nueva_marca) > 0:
            self.__marca = nueva_marca
        else:
            print("Error: Debe ingresar una marca válida.")

    def set_color(self, nuevo_color):
        if isinstance(nuevo_color, str) and len(nuevo_color) > 0:
            self.__color = nuevo_color
        else:
            print("Error: Debe ingresar un color válido.")

    def set_capacidad(self, nueva_capacidad):
        if isinstance(nueva_capacidad, (int, float)) and nueva_capacidad > 0:
            self.__capacidad = nueva_capacidad
        else:
            print("Error: Debe ingresar una capacidad válida.")

    # Método para mostrar información de la mochila
    def mostrar_info(self):
        print(f"Marca: {self.__marca}")
        print(f"Color: {self.__color}")
        print(f"Capacidad: {self.__capacidad} litros\n")
def main():
    print("=== Bienvenido al programa de mochilas ===\n")

    # Crear un objeto Mochila
    mochila1 = mochila("Nike", "Negra", 20)
    # Mostrar información de la mochila
    print("Información de la mochila:")
    mochila1.mostrar_info()
    # Actualizar la capacidad de la mochila
    nueva_capacidad = float(input("Ingrese la nueva capacidad para la mochila: "))    
    mochila1.set_capacidad(nueva_capacidad)
    # Mostrar la información actualizada de la mochila
    print("\nInformación actualizada de la mochila: ")
    mochila1.mostrar_info()
    # Actualizar el color de la mochila
    nuevo_color = input("Ingrese el nuevo color para la mochila: ")
    mochila1.set_color(nuevo_color)
    # Mostrar la información actualizada de la mochila
    print("\nInformación actualizada de la mochila: ")
    mochila1.mostrar_info()
if __name__ == "__main__":
    main()