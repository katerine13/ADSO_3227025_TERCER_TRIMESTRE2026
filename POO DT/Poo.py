class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

    
        #Vamos a crear los getter, permite acceder al valor de el atributo de forma segura
    def get_titulo(self):
        return self.__titulo
    def get_precio(self):
        return self.__precio

    
        #Vamos a controlar, validar los valores antes de ser modificados
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else:
            print("Error en el titulo ingresado, debe ser un texto valido")
    
    
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (float, int)) and nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error en el precio ingresado")
    
    
    def mostrar_info(self):
        print(f"Titulo del libro: {self.__titulo}")
        print(f"Precio : ${self.__precio}")



def main():
    print("===========S.I. de libros de Complejo Sur=============\n")
    libro1 = Libro("Pedro Paramo", 70000)  # Creamos el objeto del libro
    print("======Informacion del libro======")
    libro1.mostrar_info()

    #Mostar el precio actual
    print("\nPrecio actual del libro: $", libro1.get_precio())
    libro1.set_precio(100000) #Nuevo precio
    #Mostrar el nuevo precio
    print("\nPrecio nuevo del libro: $", libro1.get_precio())
    print("++++++ FIN DEL PROGRAMA ++++++")


if __name__ == "__main__":
    main()