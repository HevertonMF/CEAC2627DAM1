class Persona():                     # Clase para representar a una persona

  def __init__(self,minombre):                # Constructor de la clase Persona
    self.nombre = minombre
    self.emails = []
    # Agregar un email a la lista de emails de la persona

persona1 = Persona("Heverton")
persona1.emails.append("hevertonmf@gmail.com")
persona1.emails.append("info@heverton.com")
# Convertir el objeto a JSON y mostrarlo en
print(persona1)