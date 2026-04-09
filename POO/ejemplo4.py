class Operacion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

        print("Iniciando la operacion".center(50))
    
    def Calcular(self):
        print("realizando operaciones genericas")

class Suma(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion SUMA")
    
    def Calcular(self):
        super().Calcular()
        resultado = self.numero1 + self.numero2
        print(f"el resultado de la suma es: {resultado}")

def main():
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    opreacion1 = Suma(num1, num2)
    opreacion1.Calcular()

if __name__ == "__main__":
    main()