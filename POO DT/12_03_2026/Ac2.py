from abc import ABC, abstractmethod
# CREAREMOS LA CLASE ABSTRACTA
class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None  # Queda el atributo nombre como privado
        self.nombre = nombre  # Aqui llamamos al SETTER automaticamente
        
    # Crearemos los GETTER
    @property
    def nombre(self) -> str:
        # Tendra acceso seguro al nombre del empleado
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None:  # SETTER  profesional con validacion basica
        # Validaremos que sea cadena
        
        if isinstance(valor, str) and valor.strip():  # strip() quita espacios en blanco al principio y al final
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre debe ser de tipo texto.")
        
    @abstractmethod
    def trabajar(self) -> None:
        # Este metodo es obligatorio en todas las clases hijas por tener @abstractmethod 
        pass

# Crearemos las clases hijas
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta administrando toda la empresa.")
        
class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta escribiendo codigo en PYTHON.")
        
# Crearemos un Polimorfismo Activo
def ejecutar_tarea(empleado: Empleado):
    empleado.trabajar()
    
# Ejecucion didactica
def main():
    
    # Crearemos los objetos
    gerente1 = Gerente("Sebastian Herrera")
    desarrollador1 = Desarrollador("Cristian Valero")
    print("******=== POLIMORFISMO CON GETTER Y SETTER ===******".center(50))
    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
    
    print("***NOMBRES CAMBIADOS***".center(50))
    gerente1.nombre = "Tangamangapio"
    desarrollador1.nombre = "Soplamonda"
    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
if __name__ == "__main__":
    main()