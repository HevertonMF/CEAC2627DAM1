class Pedido():                                # Clase para representar a un pedido

  def __init__(self,mifecha,micliente):          # Constructor de la clase Pedido
    fecha = mifecha
    cliente = micliente
    
pedido1 = Pedido("2026-11-02","Heverton")   # Creación de un objeto de la clase Pedido
print(pedido1)
pedido2 = Pedido("2026-11-03","Juan")        # Creación de un objeto de la clase Pedido
#print pedido2
print(pedido2)