class operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print("***** ALERTA, BEEP BEEP ----- INICIALIZACION OPERACION *****")

    def calcular(self):
        print("+++++ REALIZANDO OPERACION GENERICAS +++++")

class Suma(operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion suma")

    def calcular(self):
        super().calcular()
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")

class restar(operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion resta")

    def calcular(self):
        super().calcular()
        resultado = self.numero1 - self.numero2
        print(f"El resultado de la resta es: {resultado}")

class multiplicar(operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion multiplicar")

    def calcular(self):
        super().calcular()
        resultado = self.numero1 * self.numero2
        print(f"El resultado de la multiplicacion es: {resultado}")

class dividir(operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion dividir")

    def calcular(self):
        super().calcular()
        if self.numero2 == 0:
            print("Error: El segundo número no puede ser cero.")
        else:
            resultado = self.numero1 / self.numero2
            print(f"El resultado de la division es: {resultado}")

class potencia(operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion potencia")

    def calcular(self):
        super().calcular()
        resultado = self.numero1 ** self.numero2
        print(f"El resultado de la potencia es: {resultado}")


def main():
    suma1 = Suma(32, 12)
    suma1.calcular()
    resta1 = restar(32, 12)
    resta1.calcular()
    multiplicar1 = multiplicar(32, 12)
    multiplicar1.calcular()
    dividir1 = dividir(32, 12)
    dividir1.calcular()
    potencia1 = potencia(32, 12)
    potencia1.calcular()
    print("***** ALERTA DE OPERACION YA SIN PELIGRO ----- FINALIZADA LA ALERTA *****")

if __name__ == "__main__":
    main()
