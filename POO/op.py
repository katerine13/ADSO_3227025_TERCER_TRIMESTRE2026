class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b= b
    
    def validar(self):
        if not isinstance(self.a,(int,float)) or not isinstance(self.b,(int,float)):
            raise ValueError("Los valores deben ser numericos")
        
    def mostrar_datos(self):
        print(f"Valores recibidos: {self.a} y {self.b}")

    def calcular(self):
        print("realizando operacion")

class Suma(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        resultado = self.a + self.b
        print(f"resultado de la suma {resultado}\n")

class Resta(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        resultado = self.a - self.b
        print(f"resultado de la Resta {resultado}\n")

class Multi(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        resultado = self.a * self.b
        print(f"resultado de la Multiplicaicon {resultado}\n")

class Div(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        resultado = self.a / self.b
        print(f"resultado de la Division {resultado}\n")

class Potencia(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        resultado = self.a ** self.b
        print(f"resultado de la Division {resultado}\n")

def main():
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    operacion = Resta(num1, num2)
    operacion1 = Suma(num1, num2)
    operacion2 = Multi(num1, num2)
    operacion3 = Div(num1, num2)
    operacion4 = Potencia(num1, num2)
    operacion.calcular()
    operacion1.calcular()
    operacion2.calcular()
    operacion3.calcular()
    operacion4.calcular()

    if num2 == 0:
        print("no se puede dividir")
    

if __name__ == "__main__":
    main()