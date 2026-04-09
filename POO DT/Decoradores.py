class libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

"""
#Getter permite acceder al valor de forma
    def get_precio(self):
        return self.__precio
"""

@property   #getter profesional
def precio(self):
    return self.__precio

@property
def titulo(self):
    return self.__titulo

def main():
    libro1 = libro("El coronel", 32444)
    print(libro1.precio)
    print(libro1.titulo)
    
    if __name__ == "__main__":
        main()

