import json
import os

# El json se guarda en la misma carpeta que este .py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# [{ = Tengo una lista de diccionarios
Ciclistas = []

print("=" * 40)
print("     🚴 PROGRAMA CICLISTAS JSON v0.1")
print("=" * 40)

# while True para un bucle infinito, para que el programa no se cierre hasta que el usuario lo decida
while True:
  print()
  print("┌─────────────── MENÚ ───────────────┐")
  print("│ 1. Insertar un registro            │")
  print("│ 2. Listar registros                │")
  print("│ 3. Guardar registros en disco      │")
  print("│ 4. Salir                           │")
  print("└────────────────────────────────────┘")
  opcion = input("👉 Tu opción: ")

  # Insertar un registro
  if opcion == "1":
    print("\n--- NUEVO CICLISTA ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    tipo_de_bicicleta = input("Tipo de bicicleta: ")
    # A la lista le añadimos un diccionario
    Ciclistas.append({"nombre":nombre,"apellidos":apellidos,"email":email,"Tipo de bicicleta":tipo_de_bicicleta})
    print("✅ Ciclista añadido correctamente")

  # Listar registros
  elif opcion == "2":
    print("\n--- LISTA DE CICLISTAS ---")
    if len(Ciclistas) == 0:
      print("⚠️  No hay ciclistas registrados")
    for i, c in enumerate(Ciclistas, 1):
      print(f"{i}. {c['nombre']} {c['apellidos']}")
      print(f"   📧 {c['email']}")
      print(f"   🚲 {c['Tipo de bicicleta']}")

  # Guardar registros en disco
  elif opcion == "3":
    archivo = open("ciclistas.json", 'w', encoding='utf-8')
    json.dump(Ciclistas, archivo, ensure_ascii=False, indent=2)
    archivo.close()
    print(f"💾 {len(Ciclistas)} registros guardados en ciclistas.json")

  # Salir
  elif opcion == "4":
    print("👋 ¡Hasta luego!")
    break

  else:
    print("❌ Opción no válida, prueba otra vez")
