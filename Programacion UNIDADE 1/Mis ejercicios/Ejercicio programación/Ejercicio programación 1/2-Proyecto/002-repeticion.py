"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    meta_km = input("¿Cuál es tu meta de kilómetros?: ")
    meta_km = float(meta_km)

    numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
    numero_pedaladas = int(numero_pedaladas)

    # Ahora hacemos los cálculos
