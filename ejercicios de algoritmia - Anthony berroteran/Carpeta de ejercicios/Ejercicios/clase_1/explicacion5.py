class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

    # vamos a crear los getter, permite acceder al valor de el atributo de forma segura.
    def get_titulo(self):
        return self.__titulo

    def get_precio(self):
        return self.__precio
    
    # vamos a controlar, validar los valores antes de ser modificados.
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else:
            print("Error en el titulo ingresado, debe ser un texto valido")

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float) ) and nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error en el precio ingresado, debe ser un valor valido")

    def mostrar_info(self):
        print(f"titulo del libro: {self.__titulo}")
        print(f"precio del libro: ${self.__precio}")
    

def main():
    print("S.I. de libros de Complejo Sur")
    libro1 = Libro("Pedro Paramo", 70000) #creamos el objeto libro
    print("========informacion del libro========")
    libro1.mostrar_info()


    # mostrar el precio actual
    print("\nprecio actal del libro: $", libro1.get_precio())
    libro1.set_precio(100000) #nuevo precio
    #mostrar el precio nuevo
    print("\nprecio nuevo del libro: $", libro1.get_precio())
    print("+++++ FIN DEL PROGRAMA +++++")






if __name__ == "__main__":
        main()
        