roles_usuarios =("administrador", "Analista", "gerente", "auditor")
#Ordenada por orden de ingreso
print(roles_usuarios[1])
for rol in roles_usuarios:
    print(rol)
    
print(roles_usuarios[0])
for rol in roles_usuarios:
    print(rol)
import random
nombres=["Kelly","Cristian", "Nelson","Sra Paka","Ñeno","Sebastian"]

nombre_secreto= random.choice(nombres)

print("===== ADIVINA EL CHATO=====")
print("Tiene 3 intentos de vida,,")
vidas = 3
while vidas > 0:
     for nombre in nombres:
         print(nombre)
     intento = input ("Ingresa el nombre del CHATO; ")
     if intento.lower() == nombre_secreto.lower():
        print("CHATO Ganaste,Adivina el nombre...") 
        break 
else:
        vidas =1
        print("ERROR CRITICO, el nombre del chato no es. Intentos restantes:", vidas)
        if vidas == 0:
            print("PAILAS, PERDISTE EL NOMBRE ERA", nombre_secreto, "AHORA CONSIGNA A MI NEQUI....")
            
            

# EJERCICIO DE GESTION DE CLIENTES EN UNA TIENDA
#Agregar nuevos clientes
#Recorrer la lista y mostrar todos los datos
#Modificar un nombre en caso de error
#Utilizar un cliente

#Funciones que utilizaremos
#len ()-> cuenta la instancias dentro de la fila 
#append() añade a la lista
# title()coloca el primer caracter en mayuscula ej, carlos. Carlos 
# pop() elimina un dato de la lista

#Agregar nuevos clientes

def agregar_clientes(lista_clientes, nombre):
    # Verificamos si el dato ingresado sea una cadena 
    if isinstance(nombre, str) and 2 <= len(nombre) <=50:
        #Si el nombre cumple
        lista_clientes.append(nombre.title())
        print(f"Clientes agregado:{nombre.title()}")
    else: #El nombre ingresado no cumple la validicion entonces
        print("Nombre del clientes invalido debe tener entre 2 a 50 caracteres")
def mostrar_cliente(lista_clientes):
    for clientes in lista_clientes:
        print(f"{clientes}")
def modificar_clientes(lista_cliente, indice, nuevo_nombre):
    #Verificar si el dato ingresado sea una cadena y longitud valida entre 2 a 50 caracteres
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <=len(lista_cliente):
        original = lista_cliente[indice]
        lista_cliente[indice] = nuevo_nombre.title()
        print(f"Cliente {original} fue modificado por: {nuevo_nombre.title()}")
    else:
        print("No existe ese cliente en la lista")
        # Eliminar un cliente
        # Vamos a eliminar un cliente de la lista por indice
def eliminar_cliente(lista_cliente, indice):
    if 0 <= indice <=len(lista_cliente):
        eliminado = lista_cliente.pop(indice) # Elimina el cliente de acuerdo a el numero de indice 
        # Mostraremos el registro eliminado 
        print(f"Cliente eliminado: (eliminado)")
    else:
        print("Ese cliente no existe en nuestro sistema")
def main():
    clientes =["Kelly","Cristian", "Nelson", "Sra paka", "Ñano", "Sebastian"],
    print("Clientes activos")
    mostrar_cliente(clientes, "Alejandro")
    agregar_clientes(clientes, "alejandro")
    print("Clientes activos mas el nuevo")
    mostrar_cliente(clientes)
    eliminar_cliente(clientes, "Ñano")
if __name__  == "__main__":
    main()
    
#Agregar nuevos proyectos 
#Insertar productos en una posicion especifica 
#Eliminar productos agotados
#Ordenar productos por nombre y precio 
#Invertir