class Cliente():
  def __init__(self,minombre,misapellidos,miemail,mitelefono):
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():
  def __init__(self,mifecha,minombre,misapellidos,miemail,mitelefono):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos,miemail,mitelefono)
    

pedido1 = Pedido("2026-11-02","Heverton","Marques","hevertonmf@gmail.com","662353018")

print(pedido1)