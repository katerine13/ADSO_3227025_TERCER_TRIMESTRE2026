class Muebles:      #Crea la clase

    def __init__(self, Tipo, Alto, Largo, Ancho, Color, Precio):     #Constructor
        self.__Tipo = Tipo   #Atributos, __ que es privado
        self.__Ato = Alto
        self.__Largo = Largo
        self.__Ancho = Ancho
        self.__Color = Color
        self.__Precio = Precio


  
    def get_Tipo(self):
        return self.__Tipo
    def get_Alto(self):
        return self.__Alto
    def get_Largo(self):
        return self.__Largo
    def get_Ancho(self):
         return self.__Ancho
    def get_Color(self):
        return self.__Color
    def get_Precio(self):
        return self.__Precio
        


    def mostrar_info(self):
        print (f"El tipo es: {self.__Tipo}, El alto es: {self.__Alto}, El largo es: {self.__Largo}, El ancho es: {self.__Ancho}, El color es: {self.__Color}, El  es: {self.__Precio}\n")

    

    def set_Tipo(self, nuevo_Tipo):
        if isinstance (nuevo_Tipo, str) and len(nuevo_Tipo) > 0:
            self.__Tipo = nuevo_Tipo
    def set_Color(self, nuevo_Color):
        if isinstance (nuevo_Color, str) and len(nuevo_Color) > 0:
            self.__Color = nuevo_Color
    def set_Precio (self, nuevo_Precio):
        if isinstance(nuevo_Precio, (int, float)) and nuevo_Precio > 0:
            self.__Precio = nuevo_Precio
        else:
            print("Recuerde debe ingresar un numero valido")



def main():
    # Aqui invoco los metodos
    print("=====ESTIMADO CLIENTE BIENVENIDO A LA VENTA DE MUEBLES=====\n")

# VAMOS A CREAR 2 OBJETIVOS LIBRO, UNO ES HTML Y PRECIO 1000000
# EL SEGUNDO LIBRO SERA JAVASCRIP, PRECIO $500000
    tipo1 = Muebles   ("TIPO"       "SOFA CAMA")
    alto1 = Muebles   ("ALTURA"     "1.20m")
    largo1 = Muebles  ("LARGO"      "1.50m")
    ancho1 = Muebles  ("ANCHO"      "1.10m a 2.0m")
    color1 = Muebles  ("COLOR"      "Azul Rey")
    precio1 = Muebles ("PRECIO",     1000000)

# AHORA VAMOS A MOSTRAR LOS VALORES INICIALES DEL LIBRO 1
    print("\nINFORMACION DEL MUEBLE METODOS SEPARADOS")
    print(f"El Tipo es: {tipo1.get_Tipo()}")
    print(f"El Alto es: {alto1.get_Alto()}")
    print(f"El Largo es: {largo1.get_Largo()}")
    print(f"El Ancho es: {ancho1.get_Ancho()}")
    print(f"El Color es: {color1.get_Color()}")
    print(f"El Precio es: {precio1.get_Precio()}")

# VAMOS A MOSTRAR LO ANTERIOR PERO CON TODO EL METODO MOSTRAR
    print("\nINFORMACION DEL TIPO DEL MUEBLE")
    tipo1.mostrar_info()
    print("\nINFORMACION DEL ALTO DEL MUEBLE")
    alto1.mostrar_info()
    print("\nINFORMACION DEL LARGO DEL MUEBLE")
    largo1.mostrar_info()
    print("\nINFORMACION DEL ANCHO DEL MUEBLE")
    ancho1.mostrar_info()
    print("\nINFORMACION DEL COLOR DEL MUEBLE")
    color1.mostrar_info()
    print("\nINFORMACION DEL PRECIO DEL MUEBLE")
    precio1.mostrar_info()

# Ahora vamos a actualizar el precio del libro
    print("\nACTUALIZACION DEL PRECIO DEL PRIMER LIBRO")
    nuevo_precio = float(input("Ingrese el nuevo precio"))
    tipo1.set_precio()

    print("El nuevo precio actualizado del mueble es:")
    tipo1.mostrar_info()

# Ahora actualizaremos el nombre del libro
    print("\nACTUALIZACION DEL COLOR DEL MUEBLE")
    nuevo_titulo = input("Ingrese el nuevo titulo es")
    color1.set_titulo(nuevo_titulo)
    print("El nuevo nombre actualizado del libro1 es")
    color1.get_titulo()

    print("\nLos datos actualizados del libro1 son")
    color1.mostrar_info()

    if __name__ == "__main__":
        main()