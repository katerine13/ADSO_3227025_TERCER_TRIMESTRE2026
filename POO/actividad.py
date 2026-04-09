class muebles:
    def __init__(self, nombre, color, material, precio, calidad):
        self.__nombre = nombre
        self.__color = color
        self.__precio = precio
        self.__material = material
        self.__calidad = calidad
    def get_nombre(self):
        return self.__nombre
    def get_color(self):
        return self.__color
    def get_material(self):
        return self.__material
    def get_precio(self):
        return self.__precio
    def get_calidad(self):
        return self.__calidad
    def mostrar_info(self):
        print(f"el nombre de el mueble es: {self.__nombre}, el color es: {self.__color}, el precio es: {self.__precio}, el material es: {self.__material}, y las calidad son: {self.__calidad}")

    def set_nombre(self, nuevo_nombre):
        if isinstance (nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("debe ingresar el nombre del articulo")
    
    def set_color(self, nuevo_color):
        if isinstance (nuevo_color, str) and len(nuevo_color) > 0:
            self.__color = nuevo_color
        else:
            print("debe ingresar el color del articulo")

    def set_material(self, nuevo_material):
        if isinstance (nuevo_material, str) and len(nuevo_material) > 0:
            self.__material = nuevo_material
        else:
            print("debe ingresar el material del articulo")

    def set_precio(self, nuevo_precio):
        if isinstance (nuevo_precio, (float, int)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("debe ingresar el precio")
    
    def set_calidad(self, nueva_calidad):
        if isinstance (nueva_calidad, str) and len (nueva_calidad) > 0:
            self.__calidad = nueva_calidad

def main():
    print("Bienvenido al selector de muebles")

    muebles1 = muebles("silla", "rojo", "madera", 20000, "alta")

    print("La informacion del mueble es: \n")
    muebles1.mostrar_info()

    print("\nEl nuevo mueble es")
    nuevo_nombre = input("Ingrese el nuevo meble: ")
    muebles1.set_nombre (nuevo_nombre)
    
    print("\nEl nuevo color es")
    nuevo_color = input("Ingrese el nuevo color: ")
    muebles1.set_color (nuevo_color)

    print("\nEl nuevo material es")
    nuevo_material = input("Ingrese el nuevo material: ")
    muebles1.set_material (nuevo_material)

    print("\nEl nuevo precio es")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    muebles1.set_precio (nuevo_precio)

    print("\nLa nueva calidad es")
    nueva_calidad = input("la nueva calidad es: ")
    muebles1.set_calidad (nueva_calidad)

    muebles1.mostrar_info()


if __name__ == "__main__":
    main()