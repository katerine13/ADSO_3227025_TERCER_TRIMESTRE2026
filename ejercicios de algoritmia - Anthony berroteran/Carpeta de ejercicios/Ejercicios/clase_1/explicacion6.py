from dataclasses import dataclass
@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float

    # ahora crearemos los GETTER
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
    
    # ahora crearemos los SETTER
    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "" and nuevo_titulo.strip():
            self.__titulo = nuevo_titulo
        else:
            raise ValueError("El titulo debe ser un texto valido y no vacio\n")
        
    @autor.setter
    def autor(self, nuevo_autor: str) -> None:
        if isinstance(nuevo_autor, str) and nuevo_autor !="" and nuevo_autor.strip():
            self.__autor = nuevo_autor
        else:
            raise ValueError("el autor debe ser un texto valido y no vacio\n")
        
    @isbn.setter
    def isb(self, nuevo_isbn: str) -> None:
        if isinstance(nuevo_isbn, str) and nuevo_isbn !="" and nuevo_isbn.strip():
            self.__isbn = nuevo_isbn
        else:
            raise ValueError("el isbn debe ser un texto valido y no vacio\n")
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = float(nuevo_precio)
        else:
            raise ValueError("el precio debe de ser un numero positivo\n")

    def __repr__(self) -> str:
        return(
            f"Libro(titulo = '{self._titulo}',"
            f"autor = '{self._autor}',"
            f"isbn = '{self._isbn})', "
            f"precio = {self._precio})")
    
    #PROGRAMA PRINCIPAL - DEMOSTRACION

def main():
    print("*********** PROGRAMA PRINCIPAL DE LIBRO ************")
    libro1 = Libro("Pedro Paramo","Cristian Valero","JK-322-3", 500000)
    print("*********** INFORMACION DEK KIBRO ***********")
    print(libro1)
    libro1.precio = 115000
    libro1.titulo = "Luisiño y sus travesuras"
    libro1.autor = "Andres Riaño"

    print("\n**** DATOS ACTUALIZADOS ****")
    print(libro1)
if __name__ == "__main__":
    main()