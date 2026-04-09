class Animal:
    def hacer_sonido(self):
        print("el animal hace un sonido\n".center(50))

class Perro(Animal):
    def hacer_sonido(self):
        print("el perro ladra")

class Gato(Animal):
    def hacer_sonido(self):
        print("el gato mauya")

class Tigre(Animal):
    def hacer_sonido(self):
        print("el tigre resopla")

class Leon(Animal):
    def hacer_sonido(self):
        print("el tigre ruge")

class Delfin(Animal):
    def hacer_sonido(self):
        print("el delfin cruje")

def main():
    animal1 = Animal()
    animal1.hacer_sonido()

    perro1 = Perro()
    perro1.hacer_sonido()

    gato1 = Gato()
    gato1.hacer_sonido()

    tigre1 = Tigre()
    tigre1.hacer_sonido()

    leon1 = Leon()
    leon1.hacer_sonido()

    delfin1 = Delfin()
    delfin1.hacer_sonido()


if __name__ == "__main__":
    main()