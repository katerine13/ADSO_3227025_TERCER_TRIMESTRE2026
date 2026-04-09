from abc import ABC, abstractmethod

class GenerarReporte(ABC):

    @abstractmethod
    def generar_reporte(self) -> None:
        pass

class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto # atributo comun sin privar
    
    @abstractmethod
    def procesar_pago(self) -> None:
        # metodo obligatorio definido en la clase abstracta
        pass

class PagoBancario(SistemaPago, GenerarReporte):
    def generar_reporte(self) -> None:
        print("REPORTE: Pago realiaz mediante sistema bancario")

    def Generar_pago(self) -> None:
        print(f"Procesando la transferencia bancaria por ${self.monto:,.2f}")

class PagoCriptomoneda(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"Procesando pago CRIPTO MONEDA, por ${self.monto:,.2f}")
    
def ejecutar_pago(pago: SistemaPago) -> None:
    pago.procesar_pago()

def main():
    
    print("********** === SISTEMA DE PAGOS ON INTERFASES ABSTRACTAS === **********")
    pago1 = PagoBancario(30000)
    pago2 = PagoCriptomoneda(50000)
    ejecutar_pago(pago1)
    pago1.generar_reporte()
    print("\n Ahora con criptos")
    ejecutar_pago(pago2)

if __name__ == "__main__":
    main()



        