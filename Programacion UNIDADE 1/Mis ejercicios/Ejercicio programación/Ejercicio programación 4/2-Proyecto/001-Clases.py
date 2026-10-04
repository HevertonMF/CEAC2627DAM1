# Librería de clases de la aplicación de ciclistas


# Defino lo que es una persona
class Persona():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__email = email  # privado: solo se toca con get/set

    # Métodos para leer y cambiar el email privado
    def get_email(self):
        return self.__email

    def set_email(self, email):
        if Persona.validar_email(email):
            self.__email = email
        else:
            print("Email no válido, no se ha cambiado")

    # Método estático: no necesita ningún objeto para funcionar
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Email:", self.__email)


# Defino lo que es un ciclista (hereda de Persona)
class Ciclista(Persona):
    def __init__(self, nombre, apellidos, email, equipo, bicicleta):
        super().__init__(nombre, apellidos, email)
        self.equipo = equipo
        self.bicicleta = bicicleta

    def mostrar(self):
        super().mostrar()
        print("Equipo:", self.equipo)
        print("Bicicleta:", self.bicicleta)
