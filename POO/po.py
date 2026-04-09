class Vehiculo:
    def mover(self):
        print("el vehiculo se esta moviendo")

class Carro(Vehiculo):
    def mover(self):
        print("el carro tiene 4 puertas")

class Moto(Vehiculo):
    def mover(self):
        print("la moto filtra entre los autos")

class Avion(Vehiculo):
    def mover(self):
        print("el avion lleva a los destinos rapaido")

class Submarino(Vehiculo):
    def mover(self):
        print("el submarino navega por el mundo")

def main():
    vehiculo = Vehiculo()
    vehiculo.mover()

    print("ahora usamos el metodo mover desde la clase hija")
    print("vamos a heredar este metodo desde carro")

    carro1 = Carro()
    carro1.mover()

    moto1 = Moto()
    moto1.mover()

    avion1 = Avion()
    avion1.mover()

    submarino1 = Submarino()
    submarino1.mover()


if __name__ == "__main__":
    main()

