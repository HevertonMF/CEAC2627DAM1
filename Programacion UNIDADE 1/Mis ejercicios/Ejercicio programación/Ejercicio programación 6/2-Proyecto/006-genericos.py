# f) Clases y métodos genéricos
# T es un tipo "comodín": la clase sirve para guardar cualquier tipo de dato
from typing import TypeVar, Generic

T = TypeVar("T")

print("Programa Ciclistas - Genéricos")

# Clase genérica: un almacén que vale para ciclistas, bicicletas, números...
class Almacen(Generic[T]):
  def __init__(self):
    self.elementos = []

  def insertar(self, elemento: T):
    self.elementos.append(elemento)

  def listar(self) -> list[T]:
    return self.elementos

# Método genérico: devuelve el primer elemento de cualquier lista
def primero(lista: list[T]) -> T:
  return lista[0]

# La uso con diccionarios de ciclistas
ciclistas = Almacen[dict]()
ciclistas.insertar({"nombre":"Ana","Tipo de bicicleta":"Montaña"})
ciclistas.insertar({"nombre":"Luis","Tipo de bicicleta":"Carretera"})
print(ciclistas.listar())

# La misma clase con textos
bicicletas = Almacen[str]()
bicicletas.insertar("Montaña")
bicicletas.insertar("Urbana")
print(bicicletas.listar())

print("Primer ciclista:", primero(ciclistas.listar())["nombre"])
print("Primera bicicleta:", primero(bicicletas.listar()))
