from abc import ABC, abstractmethod

# crearemos la clase abstracta
class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None  #queda el atributo nombre como provado
        self.nombre = nombre # aqui llamamos al SETTER automaticamente

    # crearemos los GETTER
    @property
    def nombre(self) -> str:
        # tendra acceso seguro al nombre del empleado
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None: # SETTER profesional como validacion basica
            # valida que sea cadena
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("el nombre debe ser de tipo texto]")

    @abstractmethod
    def trabajar(self) -> None:
        #este metodo es obligatorio en todas las clases hijas por tener @abstractmethod
        pass  


# crearemos clases hijas
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta administrando toda la empresa")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta escribiendo codigo en PYTHON")

# crearemos un polimorfismo activo
def ejecutar_tarea(empleado: Empleado):
    empleado.trabajar()

# ejecucion didactica
def main():
    gerente1 = Gerente("Sebastian Herradura")
    desarrollador1 = Desarrollador("Cristian Valero")
    print("********** === POLIMORFISMO CON GETTER === **********")
    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)

    print("\n ********** === POLIMORFISMO CON SETTER === **********")
    desarrollador1.nombre = "nano rinonez"
    gerente1.nombre = "Alberto Plazas"
if __name__ == "__main__":
    main()
