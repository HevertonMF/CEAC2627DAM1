# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='ciudades',
  password='Ciudades123$',
  database='ciudades'
)

# Creo un cursor
cursor = connection.cursor()
################### PRIMERO PIDO UN PAIS ################
cursor.execute("""
	SELECT * FROM paises
  WHERE nombre = "Brasil"
  """)
filas = cursor.fetchall()
idpais = 0
for fila in filas:
  print(fila)
  idpais = fila[0]
print("el id del pais es: ",idpais)

################### AHORA PIDO SUS CIUDADES ################

cursor.execute("""
	SELECT * FROM ciudades
  WHERE pais_id = """+str(idpais)+"""
  """)
filas = cursor.fetchall()
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
