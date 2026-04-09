class usuario:
    def __init__(self, clave, email, telefono, rol):
        self._clave = clave
        self._email = email
        self._telefono = telefono
        self._rol = rol

    # Vamos a crear los getter, para acceder al valor del atributo

    def get_clave(self):
        return self._clave
    
    def get_email(self):
        return self._email
    
    def get_telefono(self):
        return self._telefono
    
    def get_rol(self):
        return self._rol
    
    # Vams a cotrolar y validar los valores antes de modificarlos

    def set_clave(self, nueva_clave):
        if isinstance(nueva_clave, str) and nueva_clave != "":
            self._clave = nueva_clave
        else:
            print("Error en la clave ingresada")

    def set_email(self, nuevo_email):
        if isinstance(nuevo_email, str) and nuevo_email != "":
            self._email = nuevo_email
        else:
            print("Error en el email ingresado")

    def set_telefono(self, nuevo_telefono):
        if isinstance(nuevo_telefono, int) and nuevo_telefono >= 0:
            self._telefono = nuevo_telefono
        else:
            print("Error con el telefono ingresado")

    def set_rol(self, nuevo_rol):
        if isinstance(nuevo_rol, str) and nuevo_rol != "":
            self._rol = nuevo_rol
        else:
            print("Error en el rol ingresado")

    def mostrar_info(self):
        print(f"la clave del usuario es: {self._clave}")
        print(f"el email del usuario es: {self._email}")
        print(f"el telefono del usuario es: {self._telefono}")
        print(f"el rol del usuario es: {self._rol}")

def main():
    print("Informacion del usuario".center(50))
    usuario1 = usuario ("lehbdhfbr", "america@rojo", 321234563, "admin")
    usuario1.mostrar_info()

if __name__ == "__main__":
    main()