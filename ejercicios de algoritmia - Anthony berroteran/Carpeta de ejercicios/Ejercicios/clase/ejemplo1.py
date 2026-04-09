class Auto:
    def __init__(self, marca, modelo, anio, color):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__color = color

    # Métodos GET
    def get_marca(self): return self.__marca
    def get_modelo(self): return self.__modelo
    def get_anio(self): return self.__anio
    def get_color(self): return self.__color

    # Métodos SET con validación
    def set_marca(self, marca):
        if isinstance(marca, str) and len(marca) > 0:
            self.__marca = marca
        else:
            print("Error: Ingrese una marca válida.")

    def set_modelo(self, modelo):
        if isinstance(modelo, str) and len(modelo) > 0:
            self.__modelo = modelo
        else:
            print("Error: Ingrese un modelo válido.")

    def set_anio(self, anio):
        if isinstance(anio, int) and 1886 <= anio <= 2030:
            self.__anio = anio
        else:
            print("Error: Año no válido.")

    def set_color(self, color):
        if isinstance(color, str) and len(color) > 0:
            self.__color = color
        else:
            print("Error: Ingrese un color válido.")

    def mostrar_info(self):
        print(f"\n--- Información del Auto ---")
        print(f"Marca: {self.__marca}\nModelo: {self.__modelo}\nAño: {self.__anio}\nColor: {self.__color}")

def main():
    print("==== GESTIÓN DE AUTOS ====")
    mi_auto = Auto("Toyota", "Corolla", 2020, "Gris")
    
    mi_auto.mostrar_info()

    # Actualización interactiva
    print("\n--- Actualizar Datos ---")
    nueva_marca = input("Ingrese la nueva marca: ")
    mi_auto.set_marca(nueva_marca)

    nuevo_modelo = input("Ingrese el nuevo modelo: ")
    mi_auto.set_modelo(nuevo_modelo)   

    nuevo_anio = int(input("Ingrese el nuevo año: "))
    mi_auto.set_anio(nuevo_anio)

    nuevo_color =  input("Ingrese el nuevo color: ")
    mi_auto.set_color(nuevo_color)


    print("\nDatos actualizados correctamente:")
    mi_auto.mostrar_info()

if __name__ == "__main__":
    main()