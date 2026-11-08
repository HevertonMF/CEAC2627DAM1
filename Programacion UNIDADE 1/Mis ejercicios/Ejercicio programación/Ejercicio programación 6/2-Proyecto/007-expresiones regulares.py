# g) Expresiones regulares para buscar patrones en cadenas
import re

print("Programa Ciclistas - Expresiones regulares")

# Patrón de un email: texto + @ + texto + . + texto
patron_email = r"^[\w.]+@[\w]+\.[a-z]+$"

emails = ["ana@gmail.com", "luis.gmail.com", "marta@hotmail.es", "pedro@"]

for email in emails:
  if re.match(patron_email, email):
    print(email, "-> válido")
  else:
    print(email, "-> NO válido")

# Busco todos los emails que hay dentro de un texto
texto = "Contactos: ana@gmail.com, luis@yahoo.es y marta@hotmail.com"
print(re.findall(r"[\w.]+@[\w]+\.[a-z]+", texto))
