'''
def agregar_mascotas(lista_mascotas, nombre):
    if isinstance (nombre, str) and 2 <= len(nombre) <= 50:
        lista_mascotas.append(nombre.title())
        print(f"La nueva mascota agregada es: {nombre.title()}")
    else:
        print("Nombre de la mascota invalido debe tener entre 2 a 50 caracteres")

def eliminar_mascotas(lista_mascotas, indice):
    if 0 <= indice <= len(lista_mascotas):
        eliminado = lista_mascotas.pop(indice)
        print(f"Mascota eliminada: {eliminado}")
    else:
        print("La mascota no se encuentra en el sistema")

def mostrar_mascotas(lista_mascotas):
    for mascotas in lista_mascotas:
        print(f"- {mascotas}")

def main():
    mascotas = ["toby", "gruñon", "beky", "chiquita", "pacho", "garrapata"]
    print("Mascotas".center(50))
    mostrar_mascotas(mascotas)
    print("Datos Modificados".center(50))
    agregar_mascotas(mascotas, "tony")
    agregar_mascotas(mascotas, "mechas")
    agregar_mascotas(mascotas, "rapunsel")
    eliminar_mascotas(mascotas, 1)
    eliminar_mascotas(mascotas, 3)
    mostrar_mascotas(mascotas)


if __name__ == "__main__":
    main()
'''

def mostrar_inventario(productos):
    if not productos:
        print("mo hay productos registrados")
        return
    for i, productos in enumerate(productos, start = 1):
        print(f"{i}, {productos ["nombre"]} - ${productos["precio"]:.2f}")
        print("valores cambiados".center(50))
        print(f"{i}, ${productos["precio"]:.2f} - {productos["nombre"]}")

def main():
    inventario = [ 
        {"nombre": "taladro", "precio": 15000},
        {"nombre": "martillo", "precio": 5000},
        {"nombre": "destornillador", "precio": 3000}
    ]
    mostrar_inventario(inventario)
if __name__ == "__main__":
    main()