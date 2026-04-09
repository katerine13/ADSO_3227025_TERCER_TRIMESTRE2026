import random

mascota_secreto= random.choice()

print("==== ADIVINA LA MASCOTA =====")
print("Tiene 1 opurtunidad,,")
vidas = 1
while vidas > 0:
    for mascota in mascota:
        print(mascota)
    intento = input ("Ingresa el nombre de la mascota: ")
    if intento.lower() == mascota_secreto.lower():
        print("MASCOTA Ganaste, Adivinaste el nombre de la mascota")
        break 

else: 
    vidas = 1
    print("ERROR CRITICO, el nombre del animal no es, Ultimo intento:", vidas)
    if vidas == 0:
        print("INCORRECTO, perdiste el nombre de la mascota, AHORA MANDAME 50 MIL A EL 3162343754")
def agregar_mascota(lista_mascota, mascota):
    if isinstance(mascota, str) and 2 <= len(mascota) <=20:
         lista_mascota.append(mascota.title())
         print(f"Mascotas agregado:{mascota.title()}")
    else:
        print("Nombre de la mascota invalido debe tener entre 2 a 20 caracteres")