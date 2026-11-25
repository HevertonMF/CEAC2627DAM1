import json
from abc import ABC, abstractmethod
from typing import final

# Clase abstracta: no se puede crear, solo heredar de ella
class Documento(ABC):
  @abstractmethod
  def mostrar(self):          # las hijas están obligadas a tener este método
    pass

# Superclase (clase padre)
class Pedido(Documento):
  def __init__(self,mifecha,micliente):
    self.fecha = mifecha
    self.cliente = micliente

  def mostrar(self):
    print("Pedido:", self.fecha, self.cliente)

# Subclase (clase hija) que hereda de Pedido
@final                        # nadie debería heredar de esta clase
class PedidoUrgente(Pedido):
  def __init__(self,mifecha,micliente,mienvio):
    super().__init__(mifecha,micliente)   # uso el constructor del padre
    self.envio = mienvio                  # y añado un dato nuevo

  def mostrar(self):          # sobrescribo el método del padre
    print("Pedido urgente:", self.fecha, self.cliente, self.envio)

# CREATE: creo los pedidos
pedido1 = Pedido("2026-11-02","Heverton")
pedido2 = PedidoUrgente("2026-11-03","Juan","24 horas")

# Los meto en una lista
pedidos = [pedido1, pedido2]

# Convierto la lista a JSON
mijson = json.dumps(pedidos, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

# Guardo el JSON en un archivo
archivo = open("pedidos.json",'w')
archivo.write(mijson)
archivo.close()

# READ: leo el archivo JSON
archivo = open("pedidos.json",'r')
datos = json.load(archivo)
archivo.close()

# Muestro los pedidos leídos
for pedido in datos:
  print(pedido)