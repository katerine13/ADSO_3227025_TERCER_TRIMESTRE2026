from abc import ABC, abstractmethod
from typing import List #Importamos la listas para uar  notaciones de listas de objetos
#==============================================
#1. Creamos la clase abstracta persona 
#==============================================

class Persona(ABC): # Declaramos la superclase persona como abstracta
    def _init_(self, nombre: str) -> None:
        self.nombre = nombre
    @property 
    def nombre(self) -> str: #Getter para el nombre de la persona
        return self.nombre # atributo privado _nombre, devuelve el nombre almacenado en el objeto 
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) ->None:
        # Ahora validamos el nuevo_nombre que sea sr
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip(): #validamos que sea stript() elimine 
            self._nombre = nuevo_nombre
        else:
            #si no cumple las condiciones del si realizamos esta exepcion para evitar estados invalidos
            raise ValueError("El nombre debe ser una cadena de errores")

    @abstractmethod 
    def presentar(self) -> None: # Este metodo debe declararse en todas las clases hijas de persona
       pass

# =====================================
# CREAREMOS LAS CLASES HIJAS 
#=====================================
class Cliente(Persona): # El cliente hereda de personal (ahora es una subclase)
    def presentar(self) -> None:
        print(f"El cliente{self.nombre}ha llegado a el restaurante")
class Empleado(Persona): #El cliente hereda de persona(Ahora es una subclase)
    @abstractmethod
    def trabajar(self) -> None: #mMetodo definifo dentro es esta clase, toda subclase de empleado debe  
        pass 
class Mesero(Empleado):
    def presentar(self) -> None:
        print(f"El mesero{self.nombre} Esta atendiendo a los comensales")
    def trabajar(self) ->  None: #implementamos al metodo abstracto presentar() y trabajar()
        print(f"El mesero {self.nombre} esta tomando pedidos.")
class Chef(Empleado):
    def presentar(self) -> None:
        print(f"El Chef {self.nombre} esta en la cocina")
    def trabajar(self) -> None:
        print(f"El chef {self.nombre} esta preparando platos deliciosos")
#===============================================
# Crearemos la clase Cocina(), pero esta no es ABC 
#===============================================
class Cocina():
    def _init_(self, chefs: List[Chef]) -> None: # Este constructor recibe los objetos  chef y los 
        self.chefs = chefs
    @property 
    def chefs(self) -> List[Chef]: # Retomamos la lista privada de los chefs 
        return self.chefs 
    @chefs.setter 
    def chefs(self, lista_chefs: List[Chef]) -> None:
        # Validamso que lista chefs y que todos los elementos sean insta
        if isinstance(lista_chefs, list) and all (isinstance(c, Chef)for c in lista_chefs):
            self.chefs = lista_chefs #Si la lista cumple lo anterior se alamecena
        else: 
            raise ValueError("Debe promocionar una lista con elementos validos del chef")
    def operar(self) -> None:
        #Mostramos el trabajo de todos los chefs 
        for chef in self.chefs: # Recorremos la lista chefs
            chef.trabajar() # llama a el metodo trabjar() de cada objeto chef 
    class Restaurante():
        def _init_(self, nombre: str) -> None:
            self.nombre = nombre
            self.clientes: list[Cliente] = []
            self.cocina = Cocina ([Chef("Manos sucias"), Chef("El chino cochina")])
    @property
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del restaurante debe ser un nombre valido")
    def agregar_Cliente(self, cliente: Cliente) -> None:
        #Simularemos el servicio del restaurante 
        print (f"\n ===== Restaurante {self.nombre} iniciando servicio ========")
        print("\nAtendiendo Clientes")
        for cliente in self.clientes: # Llamamos al metodo presentar , genera el polimorfismo
            cliente.presentar()
        print("\n COCINA EN OPETRACION")
        self.cocina.operar()

    #=================================
    # main
    #=================================
    def main():
        # Creamos el restaurante con el nombre de "La buena Mesa"
        restaurante1 = ("La buena mesa")
        #Agregamos un cliente a el restaurante 
        restaurante1.agregar.cliente(Cliente("Juan"))
        restaurante1.agregar.cliente(Cliente("Maria"))
        # SIMULADORES INCICO DE OPERACION 
        restaurante1.iniciar_servicio

    if __name__ == "_main_":
        main()


    



        
