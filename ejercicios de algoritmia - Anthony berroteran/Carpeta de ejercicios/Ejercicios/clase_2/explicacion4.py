class empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class gerente(empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario) # heredamos estos atributos del padre
        self.departamento = departamento

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")

def main():
    gerente1 = gerente("Jean Araujo", 50000, "Alta tecnologia de desarrollo IA")
    gerente1.mostrar_info()

if __name__ == "__main__":
    main()