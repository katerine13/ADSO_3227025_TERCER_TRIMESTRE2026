class animal: 
    def Sonido(self): 
        print("El animal hace un sonido.")

class gato(animal):
    def Sonido(self):
        print("El gato maulla.")

class tigre(animal):
    def Sonido(self):
        print("El tigre ruge.")

class leon(animal):
    def Sonido(self):
        print("El leon ruge fuerte.")

class delfin(animal):
    def Sonido(self):
        print("El delfin hace click.")

def main():
    animal1 = animal()
    animal1.Sonido()
    print("ahora utilizaremos el metodo Sonido() pero desde el hijo")
    print("vamos a heredar este metodo desde gato")
    gato1 = gato()
    gato1.Sonido()
    tigre1 = tigre()
    print("vamos a heredar este metodo desde tigre")
    tigre1.Sonido()
    leon1 = leon()
    print("vamos a heredar este metodo desde leon")
    leon1.Sonido()
    delfin1 = delfin()
    print("vamos a heredar este metodo desde delfin")
    delfin1.Sonido()

if __name__ == "__main__":
    main()