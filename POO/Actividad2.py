from dataclasses import dataclass
@dataclass
class catalogo:
    _precio: float
    _descripcion: str
    _cantidad: int

    # Creamos los getter
    @property
    def precio(self) -> float:
        return self._precio
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    # Ahora vamos a crear los setter
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = float(nuevo_precio)
        else:
            raise ValueError("EL precio debe ser un numero valido")
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str) -> None:
        if isinstance(nueva_descripcion, str) and nueva_descripcion != "" and nueva_descripcion.strip():
            self._descripcion = nueva_descripcion
        else:
            raise ValueError("la descripcion debe ser un texto valido y no vacio")
        
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int) -> None:
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("la cantidad debe ser un numero valido")
        
    def __repr__(self) -> str:
        return(
            f"Precio = {self._precio} \n"
            f"descripcion = {self._descripcion} \n"
            f"cantidad = {self._cantidad} \n"
        )
    
def main():
    print("programa de catalogo".center(50))
    catalogo1 = catalogo(200000, "mesa", 2)
    print(catalogo1)

    catalogo1.precio = 100000
    catalogo1.descripcion = "tocador"
    catalogo1.cantidad = 4
    print("datos actualizados".center(50))
    print(catalogo1)

if __name__ == "__main__":
    main()
        