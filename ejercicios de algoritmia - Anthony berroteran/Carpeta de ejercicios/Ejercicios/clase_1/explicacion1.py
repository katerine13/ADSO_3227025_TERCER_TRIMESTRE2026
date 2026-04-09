class Libro: #crear la clase
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

# construccion de metodos
    # getter, devuelve el valor de el atributo solicitado. get

    def get_titulo(self):
        return self.__titulo
    def get_precio(self):
        return self.__precio
    def mostrar_info(self):
        print(f"El título es: {self.__titulo}, y el precio es: {self.__precio}\n")

    #vamos a crear un metodo para cambiar el precio

    # utilizamos el setter (ser), para realizar el cambio de el valor contenido en el
    #atributo
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("recuerde debe ingresar un numero valido")
        # en el siguiente metodo vamos a cambiar el valor del atributo titulo utilizando ser
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and len(nuevo_titulo) > 0: # debe ser string y tener al menos una letra
            self.__titulo = nuevo_titulo # actualizar el atributp con el nuevo valor

def main():
    # aqui invoco los metodos
    print("======ESTADO APRENDIZ BIENVENIDO AL PROGRAMA DE LIBRO======\n")

# vamos a crear 2 objetos libro, uno es HTML, precio 20000
# el segundo libro sera JAVASCRIP, precio 186000
    libro1 = Libro("HTML", 20000)
    libro2 = Libro("JAVASCRIP", 186000)

#AHORA VAMOS A MOSTRAR LOS CALORES INICIALES DEL LIBRO 1, CON METODOS SEPARADOS
    print("\nINFORMACION DEL PRIMER LIBRO METODO SEPARADOS")
    print(f"El titulo es: {libro1.get_titulo()}")
    print(f"El titulo es: {libro1.get_precio()}")

#vamos a mostrar lo anterior pero con todo el metodo mostrar
    print("\nINFORMACION DEL PRIMER LIBRO UN METODO")
    libro1.mostrar_info()

#ahora vamos a actualizar el precio del libro
    print("\nACTUALIZACION DEL PRECIO DEL PRIMER LIBRO")
    nuevo_precio = float(input("ingrese el nuevo precio: "))
    libro1.set_precio(nuevo_precio)

    print("el nuevo precio actualizado del libro es")
    libro1.mostrar_info()

# ahora actualizaremos el nombre del libro
    print("\n ACTUALIZACION DEL nombre del PRIMER LIBRO")
    nuevo_titulo = input("INGRESE EL NUEVO TITULO: ")
    print("el nuevo nombre actualizado del libro1 es")
    libro1.get_titulo()

    print("\n  LOS DATOS ACTUALIZADOS DEL LIBRO1 SON")
    libro1.mostrar_info()

if __name__ == "__main__":
    main()