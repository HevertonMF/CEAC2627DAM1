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
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    try:
        meta_km = input("¿Cuál es tu meta de kilómetros?: ")
        meta_km = float(meta_km)

        numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print("Entrada inválida. Por favor, introduce solo números.")
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")

    # Preguntamos si el usuario quiere hacer otro cálculo o salir del programa
    print()
    continuar = input("¿Quieres calcular otra vez? (s/n): ")

    # Si no responde "s", rompemos el bucle y terminamos el programa
    if continuar.lower() != "s":
        print("¡Hasta luego!")
        break
