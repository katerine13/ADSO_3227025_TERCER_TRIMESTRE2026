from abc import ABC, abstractmethod
from typing import List # importamos listas para usar notaciones de lista de objetivos

# =============================================
# 1. Crearemos la clase abstracta persona
# =============================================

class Persona(ABC): # declaramos la superclase persona como abstracta
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    
    @property
    def nombre(self) -> str: # GETTER para el nombre de la persona
        return self._nombre # atributo privado_nombre, devuelve el nombre almacenado en el objeto

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        # ahora validamos el nuevo_nombre que sea str
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip(): # validamos que strip() elimine los espacios en blanco
            self._nombre = nuevo_nombre
        else:
            # si no cumple las condiciones del si realizamos esta excepcion para evitaar estados invalidos
            raise ValueError("el nombre debe ser una cadena de caracteres")
    @abstractmethod
    def presentar(self) -> None: # este metodo debe e=decararse en todas las calases hijas de persona
        pass

# ==============================
# CREAREMOS LAS CLASES HIJAS
# ==============================

class Cliente(Persona): # el cliente hereda de persona ( ahora es una subclase )
    def presentar(self) -> None:
        print(f"El cliente {self.nombre} ha llegar al restaurante")

class Empleado(Persona): # el cliente hereda de persona ( ahora es una subclase )
    @abstractmethod
    def trabajar(self) -> None: # metodo definido dentro es esta clase, toda subclase de empleado debe implementarlo
        pass

class Mesero(Empleado): 
    def presentar(self) -> None: # implementamos el metodo abstracto presentar() y trabajar()
        print(f"mesero {self.nombre} atendiendo a los comensales")
    def trabajar(self) -> None:
        print(f"el mesero {self.nombre} esta tomando pedidos")

class Chef(Empleado): 
    def presentar(self) -> None:
        print(f"chef {self.nombre} esta en la cocina")
    def trabajar(self) -> None: # implementamos el metodoo asbtracto presentar() y trabajar()
        print(f"el chef {self.nombre} esta preparando platos deliciosos")

# ===================================================
# Crearemos la clase cocina(), pero esta no es ABC
# ===================================================

class Cocina():
    def __init__(self, chefs: List[Chef]) -> None: # este constructor recibe los objetos chef y los almacena en una lista
        self.chefs = chefs
    @property
    def chefs(self) -> List[Chef]: # retornamos la lista privada de _chefs
        return self.chefs
    @chefs.setter
    def chefs(self, lista_chefs: List[Chef]) -> None:
        #validamos que lista_chefs y que todos los elementos sean instancias de class Chef
        if isinstance(lista_chefs, list) and all(isinstance(c, Chef) for c in lista_chefs):
            self.chefs = lista_chefs #si la lista cumple lo anterior se almacena
        else:
            raise ValueError("Debe proporcinar una lista con elementos validos de chef")
        
    def operar(self) -> None:
        # mostraremos el trabajo de todos los chef 
        for chef in self.chefs: # recorremos la lista chefs
            chef.trabajar() #llama el metodo trabajar() de cada objeto chef

class Restaurante():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.cliente: List[Cliente]
        self.cocina = Cocina([Chef("Manos sucias")])


    @property
    def nombre(self) -> None:
        return self.nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("el nombre del restaurante debe ser un nombre valido")
        
    def agregar_cliente(self, cliente: Cliente) -> None:
        if isinstance(cliente, Cliente):
            self.cliente.append(cliente) # append agregar a la lista
        else: 
            raise ValueError("el nombre del cliente debe de ser un nombre valido")

    def iniciar_servicio(self) -> None:
        #simularemos el servicio del restaurante
        print(f"\n=====Restaurante {self.nombre} iniciando servicio")
        print(f"\nAtendiendo cliente")
        for cliente in self.cliente: # llamados al metodo presentar, genera el polimorfismo
            cliente.presentar()

        print("\n COCINA EN OPERACION:")
        self.cocina.operar()

# ===========
# main
# ===========

def main() -> None:
    # crearemos el restaurante con el nombre "La Buena Mesa"
    restaurante = Restaurante("La Buena Mesa")
    # agregarmos dos clientes al restaurante
    restaurante.agregar_cliente(Cliente("JUAN"))
    restaurante.agregar_cliente(Cliente("Maria"))
    # SIMULAREMOS INICIO DE OPERACION 
    restaurante.iniciar_servicio()

if __name__ == "__main__":
    main()