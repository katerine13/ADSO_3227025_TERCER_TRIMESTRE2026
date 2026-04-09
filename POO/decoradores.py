class libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
        
    @property
    def precio(self):
        return self.__precio
    
    @property
    def titulo(self):
         return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
         if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo

    @precio.setter
    def precio(self, nuevo_precio):
        """setter con validacion de seguridad"""
        if isinstance(nuevo_precio, (int,float)) and nuevo_precio >0:
              self.__precio = nuevo_precio
        else:
            print("el precio debe ser un numero positivo")

    def mostrar_info(self):
        print(f"titulo: {self.__titulo}")
        print(f"precio: ${self.__precio:,.2f}")


    
    
def main():
    libro1 = libro("El coronel", 34400)
    print(libro1.precio)
    print(libro1.titulo)
        
    print("\nActualizando titulo")
    libro1.titulo = "hola"
    print(libro1.titulo)

    print("\nActualizando precio")
    libro1.precio = 35500.345
    print(libro1.precio)
    print("nuevo precio",libro1.precio)

    print("nuevos datos del libro\n")
    print(libro1.mostrar_info())

if __name__ == "__main__":
    main()