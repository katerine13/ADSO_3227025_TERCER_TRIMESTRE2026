class Opreracion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print("**** ALERTA Beep Beep Iniciando la Operacion****" \
        "")

    def calcular(self):
        print("++++ REALIZANDO OPERACIONES GENERICAS++++")

class Suma(Opreracion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operacion SUMA")
    
    def calcular(self):
        super().calcular() # Reutilizando el metodo calcular pero del padre
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")

def main():
    num1 = float(input("Ingrese el primer numero"))
    num2 = float(input("Ingrese el segundo numero"))
    Opreracion1 = Suma(num1, num2)
    Opreracion1.calcular()

if __name__ == "__main__":
    main()