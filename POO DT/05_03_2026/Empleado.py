class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario) # Hereda estos atributos del padre
        self.departamento = departamento

    def mostrar_info(self):
        print(f"Nombre:  {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")

def main():
    
    gerente1 = Gerente("Cristian Valero", 5000, "Alta Tecnologia de Desarrollo IA")
    gerente1.mostrar_info()


if __name__ == "__main__":
    main()