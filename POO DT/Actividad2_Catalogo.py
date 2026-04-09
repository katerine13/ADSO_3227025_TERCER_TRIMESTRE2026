from dataclasses import dataclass

@dataclass
class Catalogo:
    _precio: float
    _descripcion: str
    _cantidad: float
    
    # Ahora crearemos los GETTER
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def cantiadad(self) -> float:
        return self._cantidad
    
    # Ahora crearemos los SETTER
    
    @precio.setter
    def precio(self, nuevo_precio: float)  -> None:
        if isinstance(nuevo_precio, (float, int)) and nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser un texto valido y no vacio\n")
        
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str)  -> None:
        if isinstance(nueva_descripcion, str) and nueva_descripcion != "" and nueva_descripcion.strip():
            self._descripcion = nueva_descripcion
        else:
            raise ValueError("Debe ingresar una descripcion valida\n")
        
    @cantiadad.setter
    def cantidad(self, nueva_cantidad: float)  -> None:
        if isinstance(nueva_cantidad, (float, int)) and nueva_cantidad > 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad debe ser mayor a 0\n")
        
    def __repr__(self) -> str:
        return (
            f"Precio = {self._precio} \n"
            f"Descripcion = {self._descripcion} \n"
            f"Cantidad = {self._cantidad} \n" 
        )
        
#Progrma principal
        
def main():
    print("     ****************Catalogo***************")
    Libro1 = Catalogo(500000, "Es alto, bajo y ancho ideal para soporte de microfono profesional con alta resisitencia", 2)
    print("  **************Informacion de clase***********")
    print(Libro1)
    
if __name__ == "__main__":
    main()