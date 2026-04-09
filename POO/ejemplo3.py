class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departemento):
        super().__init__(nombre, salario)
        self.departamento = departemento
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")

def main():
    gerente1 = Gerente("Nelson", 2000, "Alta de tecnologia de desarrollo")
    gerente1.mostrar_info()

if __name__ == "__main__":
    main()