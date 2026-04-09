class Libro:    

    def __init__(self, titulo, precio):
        self._titulo = titulo
        self._precio =  precio

    @property

    def precio(self):
        return self._precio

    @property

    def titulo(self):
        return self._titulo

    @titulo.setter

    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self._titulo = nuevo_titulo

    @precio.setter

    def precio(self, nuevo_precio):
        """Setter con validación de seguridad."""
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self._precio = nuevo_precio

        else:
            print("El precio debe ser un número positivo.")

    def mostrar_info(self):
        print(f"Título: {self._titulo}")
        print(f"Precio: ${self._precio:,.2f}")

def main():

    librol = Libro("El coronel", 3232)
    print(librol.precio)

    print("\nActualizando titulo...")

    librol.titulo = "hola"
    print(librol.titulo)

    print("\nActualizando precio")
    librol.precio = 150000.326
    print(librol.precio)

    print(f"nuevo precio: ${librol.precio:,.2f}")
    print (f"Nuevos datos del libro\n")

    print(librol.mostrar_info())

if __name__ == "__main__":
    main()