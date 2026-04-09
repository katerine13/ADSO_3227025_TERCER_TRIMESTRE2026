from abc import ABC, abstractmethod
class GenerarReporte(ABC):
    @abstractmethod
    def generar_repote(self) -> None:
        pass

class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto  # Atributo comun sin privar
    @abstractmethod
    def procesar_pago(self) -> None:
        # Metodo obligatorio definido en la clase abstracta
        pass

class PagoBancario(SistemaPago, GenerarReporte):
    def generar_repote(self) -> None:
        print("REPORTE: Pago realizado mediante sistema bancario")
    def procesar_pago(self) -> None:
        print("Procesando la transferencia bancaria por ${self.monto:,.2f}")
        
class PagoCriptomoneda(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"Procesando pago CRIPTO MONEDAS, por $ {self.monto:,.2f}")
        
def ejecutar_pago(pago: SistemaPago) -> None:
    pago.procesar_pago()
    
def main():
    print("***=== SISTEMA DE PAGOS DE INTERFACES ABSTRACTAS ===***")
    pago1 = PagoBancario(30000)
    pago2 = PagoCriptomoneda(50000)
    ejecutar_pago(pago1)
    pago1.generar_repote()
    print("\nAhora con criptos")
    ejecutar_pago(pago2)
    
if __name__ == "__main__":
    main()