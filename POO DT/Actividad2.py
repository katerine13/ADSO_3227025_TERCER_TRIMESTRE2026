class Usuario:
    def __init__(self, clave, email, telefono, rol):
        
        self.__clave = clave
        self.__email = email
        self.__telefono = telefono
        self.__rol = rol
        
    #Vamos a crear los getter, permite acceder al valor de el atributo de forma segura
    def get_clave(self):
        return self.__clave
    def get_email(self):
        return self.__email
    def get_telefono(self):
        return self.__telefono
    def get_rol(self):
        return self.__rol
    
    #Vamos a controlar, validar los valores antes de ser modificados
    def set_clave(self, nueva_clave):
        if isinstance(nueva_clave, str) and nueva_clave != "":
            self.__clave = nueva_clave
        else:
            print("Error en la clave ingresada, debe ser un texto valido")
            
            
    def set_email(self, nuevo_email):
        if isinstance(nuevo_email, str) and nuevo_email != "":
            self.__email = nuevo_email
        else:
            print("Error en el email ingresado, debe ser un texto valido")
            
    def set_telefono(self, nuevo_telefono):
        if isinstance(nuevo_telefono, (float, int)) and nuevo_telefono >= 0:
            self.__telefono = nuevo_telefono
        else:
            print("Error en el telefono ingresado, debe ser un nuemero valido")
            
    def set_rol(self, nuevo_rol):
        if isinstance(nuevo_rol, str) and nuevo_rol != "":
            self.__rol = nuevo_rol
        else:
            print("Error en el rol ingresado, debe ser un texto valido")
        
            
    def mostrar_info(self):
        print(f"Clave: {self.__clave}")
        print(f"Email: {self.__email}")
        print(f"Telefono: {self.__telefono}")
        print(f"Rol: {self.__rol}")
        
        
def main ():
    print("=================USUARIO================")
    libro1 = Usuario("CHAMO", "chamito123@gmail.com", 3115264898, "ADMINISTRADOR")
    print("========INFORMACION DE CLASE========")
    libro1.mostrar_info()

    
    #Mostar la clave actual
    print("\nClave actual del usuario:", libro1.get_clave())
    libro1.set_clave("Hola_Mundo") #Nueva clave
    #Mostrar la nueva clave
    print("\nClave nueva del usuario:", libro1.get_clave())

    
    #Mostar el telefono actual
    print("\nTelefono actual del usuario:", libro1.get_telefono())
    libro1.set_telefono(3103146562) #Nueva telefono
    #Mostrar el telefono nuevo
    print("\nTelefono nuevo del usuario:", libro1.get_telefono())
    print("++++++ FIN DEL PROGRAMA ++++++")


if __name__ == "__main__":
    main()