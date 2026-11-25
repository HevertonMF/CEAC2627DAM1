class Cliente():                                               # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos,miemail,mitelefono):  # Constructor de la clase Cliente
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():                                                   # Clase para representar a un pedido

  def __init__(self,mifecha,minombre,misapellidos,miemail,mitelefono): #constructor de la clase Pedido
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos,miemail,mitelefono)
    
# Creación de un objeto de la clase Cliente

pedido1 = Pedido("2026-11-02","Heverton","Marques","hevertonmf@gmail.com","662353018")
#print pedido                 

print(pedido1)