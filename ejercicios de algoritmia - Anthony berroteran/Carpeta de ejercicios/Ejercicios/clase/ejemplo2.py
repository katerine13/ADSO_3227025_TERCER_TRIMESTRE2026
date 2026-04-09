class Estudiante:
    def __init__(self, nombre, id_estudiante, carrera, promedio):
        # Atributos privados
        self.__nombre = nombre
        self.__id_estudiante = id_estudiante
        self.__carrera = carrera
        self.__promedio = promedio

    # Métodos GET
    def get_nombre(self): return self.__nombre
    def get_id(self): return self.__id_estudiante
    def get_carrera(self): return self.__carrera
    def get_promedio(self): return self.__promedio

    # Métodos SET con validación
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.__nombre = nombre
        else:
            print("Error: Nombre inválido.")

    def set_promedio(self, promedio):
        # Validamos que sea un número y esté en el rango académico estándar
        if isinstance(promedio, (int, float)) and 0.0 <= promedio <= 5.0:
            self.__promedio = promedio
        else:
            print("Error: El promedio debe estar entre 0.0 y 5.0.")

    def mostrar_info(self):
        print(f"\n--- Ficha del Estudiante ---")
        print(f"Nombre: {self.__nombre}\nID: {self.__id_estudiante}")
        print(f"Carrera: {self.__carrera}\nPromedio: {self.__promedio}")

def main():
    print("==== GESTIÓN DE ESTUDIANTES ====")
    # Instanciamos el estudiante
    estudiante = Estudiante("Juan Pérez", "102030", "Ingeniería", 4.2)
    
    estudiante.mostrar_info()

    # Actualización interactiva
    print("\n--- Actualizar Información Académica ---")
    
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    estudiante.set_nombre(nuevo_nombre)

    # Convertimos a float para el promedio
    nuevo_promedio = float(input("Ingrese el nuevo promedio (0.0 - 5.0): "))
    estudiante.set_promedio(nuevo_promedio)

    print("\nInformación actualizada:")
    estudiante.mostrar_info()

if __name__ == "__main__":
    main()