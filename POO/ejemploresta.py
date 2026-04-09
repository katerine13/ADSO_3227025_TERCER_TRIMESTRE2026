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
        print("preparando la operacion RESTA")
    
    def Calcular(self):
        super().Calcular()
        resultado = self.numero1 - self.numero2
        print(f"el resultado de la resta es: {resultado}")

def main():
    opreacion1 = Suma(19, 16)
    opreacion1.Calcular()

if __name__ == "__main__":
    main()