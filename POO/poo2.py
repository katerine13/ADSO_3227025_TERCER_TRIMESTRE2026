from dataclasses import dataclass
@dataclass
class libro:
    _titulo: str
    _precio: float
    _autor: str
    _isbn: str
    
    #creamos ahora los getter
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @property
    def isbn(self) -> str:
        return self._isbn 
    
    #ahpra creamos los setter
    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "" and nuevo_titulo.strip():
            self._titulo = nuevo_titulo
        else:
            raise ValueError("El titulo debe ser un texto valido y no vacio\n")
        
    @autor.setter
    def autor(self, nuevo_autor: str) -> None:
        if isinstance(nuevo_autor, str) and nuevo_autor != "" and nuevo_autor.strip():
            self._autor = nuevo_autor
        else:
            raise ValueError("el autor debe ser un texto valido y no vacio\n")
        
    @isbn.setter
    def isbn(self, nuevo_isbn: str) -> None:
        if isinstance(nuevo_isbn, str) and nuevo_isbn != "" and nuevo_isbn.strip():
            self._isbn = nuevo_isbn
        else:
            raise ValueError("el isbn debe ser un texto valido y no vacio\n")
        
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = float(nuevo_precio)
        else:
            raise ValueError("el precio debe ser un numero. valido y no vacio\n")
        
    def __repr__(self) -> str:
        return(
            f"libro = {self._titulo} \n"
            f"autor = {self._autor} \n"
            f"isbn = {self._isbn} \n" 
            f"precio = {self._precio} \n")
        
        
def main():
    print("Programa principal del libro".center(50))
    libro1 = libro("juanito", "andres ocampo", "232", 20000)
    print("Informacion del libro".center(50))
    print(libro1)
    libro1.precio = 11500
    libro1.titulo = "luis"
    libro1.autor = "petro"
    print("datos actualizados".center(50))
    print(libro1)


if __name__ == "__main__":
    main()
    