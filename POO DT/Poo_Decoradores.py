from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float


    # Ahora craremos los GETTER
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    @property
    def precio(self) -> float:
        return self._precio
    

    # Ahora crearemos los SETTER

    @titulo.setter
    def titulo(self, nuevo_titulo: str)  -> None:
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "" and nuevo_titulo.strip():
            self._titulo = nuevo_titulo
        else:
            raise ValueError("El titulo debe ser un texto valido y no vacio\n")
    
    @autor.setter
    def autor(self, nuevo_autor: str)  -> None:
        if isinstance(nuevo_autor, str) and nuevo_autor != "" and nuevo_autor.strip():
            self._autor = nuevo_autor
        else:
            raise ValueError("Debe ingresar un nombre valido\n")
        
    @isbn.setter
    def isbn(self, nuevo_isbn: str)  -> None:
        if isinstance(nuevo_isbn, str) and nuevo_isbn != "" and nuevo_isbn.strip():
            self._isbn = nuevo_isbn
        else:
            raise ValueError("isbn debe ser un texto valido y no vacio\n")
        
    @precio.setter
    def precio(self, nuevo_precio: float)  -> None:
        if isinstance(nuevo_precio, (float, int)) and nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser un texto valido y no vacio\n")

    def __repr__(self) -> str:
        return (
            f"Libro = {self._titulo} \n"
            f"Autor = {self._autor} \n"
            f"isbn = {self._isbn} \n" 
            f"precio = {self._precio} \n"
        )


    #PROGRAMA PRINCIPAL - DEMOSTRACION
    
def main():
        print("******************PROGRAMA PRINCIPAL DE LIBRO**************************")
        Libro1 = Libro("Pedro Paramo", "Cristian Valero", "JK-322-3", 50000)
        print("******************INFORMACION DEL LIBRO***************")
        print(Libro1)
    
if __name__ == "__main__":
    main()