class libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
        
    #vamos a crear lo getter, permite accedes al valor de el atributo de forma segura.
    def get_titulos(self):
        return self.__titulo
    
    def get_precio(self):
        return self.__precio
    
    #vamos a controlar, validar los valores antes de ser modificados
    
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else:
            print("Error en el titulo ingresado")
            
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (float,int)) and nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error el precio ingresado debe ser un numero valido")
            
    def mostrar_info(self):
        print(f"el titulo del libro: {self.__titulo}")
        print(f"el nuevo precio del libro es: {self.__precio}")
            
def main():
    print("S.I. de libros complejo sur".center(50))
    libro1 = libro ("Juanito Alimaña", 20.000)            #Creamos el objeto libro
    print("informacion del libro".center(50))
    libro1.mostrar_info()
    
    
    

if __name__ == "__main__":
    main()
        