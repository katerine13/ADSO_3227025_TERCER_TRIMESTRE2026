class Vehiculo: #esta va a ser mi clase padre
    def mover(self): # este metodo es el que vamos a heredar a los hijos
        print("**** El vehículo se está moviendo ****")

class carro(Vehiculo):
    def mover(self):
        print("**** el carro rueda por la carretera ****\n")
class moto(Vehiculo):  
    def mover(self): 
        print("**** la moto va a mil por la autopista ****\n")
class avion(Vehiculo):
    def mover(self):
        print("**** el avión vuela sobre las nubes ****\n")
class submarino(Vehiculo): 
    def mover(self):
        print("**** el submarino bucea el rio bogota ****\n")

def main():
    vehiculo = Vehiculo()
    vehiculo.mover()
    print("ahora utilizaremos el metodo mover() pero desde el hijo")
    print("vamos a herdar este metodo desde carro")
    carro1 = carro()
    carro1.mover()
    moto1 = moto()
    print("vamos a heredar este metodo desde moto")
    moto1.mover()
    avion1 = avion()
    print("vamos a heredar este metodo desde avion")
    avion1.mover()
    submarino1 = submarino()
    print("vamos a heredar este metodo desde submarino")
    submarino1.mover()

if __name__ == "__main__":
    main()