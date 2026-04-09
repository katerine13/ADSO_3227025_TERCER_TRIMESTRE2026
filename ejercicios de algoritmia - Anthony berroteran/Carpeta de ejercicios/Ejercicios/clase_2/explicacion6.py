class operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def validar(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Error: Ambos números deben ser enteros o flotantes.")
    def mostrar_datos(self):
        return(f"valores recibidos: {self.a} y {self.b}")
    
    def calcular(self):
        print("realizando operacion matematica")

class suma(operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a + self.b
        print(f"Resultado de la suma es {resultado}")

class restar(operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a - self.b
        print(f"Resultado de la resta es {resultado}")

class multiplicar(operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a * self.b
        print(f"Resultado de la multiplicacion es {resultado}")

class dividir(operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        if self.b == 0:
            print("Error: El segundo número no puede ser cero.")
        else:
            resultado = self.a / self.b
            print(f"Resultado de la division es {resultado}")

class potencia(operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a ** self.b
        print(f"Resultado de la potencia es {resultado}")

def main():
    num1 = float(input("ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero: "))
    operacion1 = suma(num1, num2)
    operacion1.calcular()

    operacion2 = restar(num1, num2)
    operacion2.calcular()

    operacion3 = multiplicar(num1, num2)
    operacion3.calcular()

    operacion4 = dividir(num1, num2)
    operacion4.calcular()

    operacion5 = potencia(num1, num2)
    operacion5.calcular()


if __name__ == "__main__":
    main()