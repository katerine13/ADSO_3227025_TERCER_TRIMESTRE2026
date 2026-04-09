'''
nombre = ["nelson", 18, 170, "Bosa", "analista y desarrollador de software", "SENA"]

nombre[4] = "estudiante"

for i in nombre:
    print(i)
'''

'''

import random

nombre = ["kelly", "cristian", "Nelson", "sra paka", "ñaño", "Sebastian", "pelu", "arley", "dylan", "jesus"]

nombre_secreto = random.choice(nombre)
print("Adivina el chato".center(50))
vidas = 3
while vidas > 0:
    for i in nombre:
        print(i)
    intento = input("Ingrese el nombre del chato: ")
    if intento.lower() == nombre_secreto.lower():
        print("Adivinaste el nombre")
        break
    else:
        vidas -= 1
        print("No has adivinado el nombre del chato", vidas)

if vidas == 0:
    print(f"Pailas, perdiste el nombre era: {nombre_secreto}")

'''

# Recorrer la lista y mostrar todos los datos
# Modificar un nombre en caso de error
# len() cuenta las instancias dentro de la lista
# append() añade datos a la lista
# title() pone la primera ñetra en mayuscula
# pop() Elimina el dato de la lista


def agregar_cliente(lista_clientes, nombre):
    if isinstance (nombre, str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f"El nuevo cliente agreagado es: {nombre.title()}")
    else:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")

def mostrar_cliente(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

def mostrar(lista_clientes):
    print(f"{lista_clientes.title()}")

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not isinstance (nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <= len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"cliente {original} fue modificado por: {nuevo_nombre.title()}")
    else:
        print("no existe ese cliente en la lista")

def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice <= len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("Ese cliente no existe en nuestro sistema")


def main():
    clientes = ["kelly", "cristian", "Nelson", "sra paka", "ñaño", "Sebastian", "pelu", "arley", "dylan", "jesus"]
    modificar_cliente(clientes, 4, "pola")
    mostrar_cliente(clientes)
    eliminar_cliente(clientes, 4)
    mostrar_cliente(clientes)
    
if __name__ == "__main__":
    main()

