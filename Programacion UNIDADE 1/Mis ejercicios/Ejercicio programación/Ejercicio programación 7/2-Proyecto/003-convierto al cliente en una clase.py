class Cliente():                                               # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos,miemail,mitelefono):         # Constructor de la clase Cliente
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():                                               # Clase para representar a un pedido

  def __init__(self,mifecha,micliente):                       # Constructor de la clase Pedido

    self.fecha = mifecha
    self.cliente = Cliente()
    
