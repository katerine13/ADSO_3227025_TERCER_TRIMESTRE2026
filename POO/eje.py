from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None  # atributo queda privado
        self.nombre = nombre # aqui llamamos a los SETTER automaticamente

    @property
    def nombre(self) -> str:
        # tendra acceso seguro al nombre del empleado
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None: # setter profesional con validacion basica
        
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()

        else:
            raise ValueError("el nombre debe ser de tipo texto")
    
    @abstractmethod
    def trabajar(self) -> None:
        # Este metodo es obligatorio en todos las clases hijas 
        pass

class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta administrando todas las empresa")
    
class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta escribiendo codigo en PYTHON")

class Vendedor(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta realizando algunas reuniones sobre ventas")

class Tecnico(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta arreglando arreglando algunos problemas de internet")

def ejecutar(empleado: Empleado):
    empleado.trabajar()


def main():
    gerente = Gerente("Andres Ocampo")
    desarrollador = Desarrollador("Christian Valero")
    vendedor = Vendedor("Pablo Neruda")
    tecnico = Tecnico("Luis Perez")
    print("Polimorfismo con GETTER Y SETTER".center(50))
    ejecutar(gerente)
    ejecutar(desarrollador)
    ejecutar(vendedor)
    ejecutar(tecnico)
    

    print("Nombres Actualizados".center(50))
    desarrollador.nombre = "ingeniero riñones"
    gerente.nombre = "ingeniero bocamonda"
    vendedor.nombre = "Pedro Picapiedra"
    tecnico.nombre = "Sebastian lara"

    ejecutar(desarrollador)
    ejecutar(gerente)
    ejecutar(vendedor)
    ejecutar(tecnico)

if __name__ == "__main__":
    main()