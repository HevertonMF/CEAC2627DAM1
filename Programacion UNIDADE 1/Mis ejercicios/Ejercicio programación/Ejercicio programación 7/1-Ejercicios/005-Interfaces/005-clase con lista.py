class Persona():
  def __init__(self,minombre):
    self.nombre = minombre
    self.emails = []
    
persona1 = Persona("Heverton")
persona1.emails.append("hevertonmf@gmail.com")
persona1.emails.append("info@heverton.com")

print(persona1)