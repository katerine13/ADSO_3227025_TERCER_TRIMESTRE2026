class padre():
    def __init__(self, mensaje):
        self.mensaje = mensaje

class hijo(padre):
    def __init__(self, mensaje, nombre):
        super().__init__(mensaje) # reutilizamos el construtor del padre
        self.nombre = nombre

def main():
    objeto1 = hijo("este mensaje desde la clase padre", "este mensaje desde la clase hijo")
    print(f"{objeto1.mensaje}, {objeto1.nombre}")
    print(objeto1.nombre)
    print(objeto1.mensaje)

if __name__ == "__main__":
    main()