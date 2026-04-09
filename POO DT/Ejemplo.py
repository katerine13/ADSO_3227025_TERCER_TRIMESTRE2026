class Libro:      #Crea la clase

    def __init__(self, titulo, precio):     #Constructor
        self.__titulo = titulo   #Atributos, __ que es privado
        self.__precio = precio

    # Contrucción de metodos

        # getter, devuelve el valor de el atributo solicitado.    get
    def get_titulo(self):   # Identifica que el va a devolver un valor y solo lo muestra
        return self.__titulo
    def get_precio(self):   # Identifica que el va a devolver un valor y solo lo muestra
        return self.__precio
        # Ahora realizaremos un metodo que muestre los dos valores

    def mostrar_info(self):
        print (f"El titulo es: {self.__titulo}, y el precio es: {self.__precio}\n")

        # Vamos a crear un metodo para cambiar el precio

        # Utilizamos el SETTER (set), para realizar el cambio de el valor contenido en el atributo
    def set_precio (self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Recuerde debe ingresar un numero valido")

        # En el siguiente metodo vamos a cambiar el valor del atributo titulo utilizando set
    def set_titulo(self, nuevo_titulo):
        if isinstance (nuevo_titulo, str) and len(nuevo_titulo) > 0:  # Debe ser string y tener al menos una letra
            self.__titulo = nuevo_titulo  # Actualiza el atributo con el valor

def main():
    # Aqui invoco los metodos
    print("=====ESTIMADO APRENDIZ BIENVENIDO AL PROGRAMA DE LIBRO====\n")

# VAMOS A CREAR 2 OBJETIVOS LIBRO, UNO ES HTML Y PRECIO $200000
# EL SEGUNDO LIBRO SERA JAVASCRIP, PRECIO $186000
    Libro1 = Libro("HTML", 200000)
    Libro2 = Libro("JAVASCRIP", 186000)

# AHORA VAMOS A MOSTRAR LOS VALORES INICIALES DEL LIBRO 1
    print("\nINFORMACION DEL PRIMER LIBRO METODOS SEPARADOS")
    print(f"El titulo es: {Libro1.get_titulo()}")
    print(f"El precio es: {Libro2.get_precio()}")

# VAMOS A MOSTRAR LO ANTERIOR PERO CON TODO EL METODO MOSTRAR
    print("\nINFORMACION DEL PRIMER LIBRO UN METODO")
    Libro1.mostrar_info()

# Ahora vamos a actualizar el precio del libro
    print("\nACTUALIZACION DEL PRECIO DEL PRIMER LIBRO")
    nuevo_precio = float(input("Ingrese el nuevo precio"))
    Libro1.set_precio(nuevo_precio)

    print("El nuevo precio actualizado del libro es")
    Libro1.mostrar_info()

# Ahora actualizaremos el nombre del libro
    print("\nACTUALIZACION DEL NOMBRE DEL PRIMER LIBRO")
    nuevo_titulo = input("Ingrese el nuevo titulo es")
    Libro1.set_titulo(nuevo_titulo)
    print("El nuevo nombre actualizado del libro1 es")
    Libro1.get_titulo()

    print("\nLos datos actualizados del libro1 son")
    Libro1.mostrar_info()

if __name__ == "__main__":
    main()