"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""


# ------------------------------------------------------------------
# Códigos ANSI para dar color y estilo al texto en la terminal
# No necesitan ninguna librería externa
# ------------------------------------------------------------------
class Color:
    RESET = "\033[0m"
    NEGRITA = "\033[1m"
    CIAN = "\033[96m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    GRIS = "\033[90m"


ANCHO = 50


def linea():
    """Imprime una línea separadora para dividir visualmente las secciones"""
    print(Color.GRIS + "─" * ANCHO + Color.RESET)


def titulo(texto):
    """Imprime un título centrado, con color y rodeado de una caja simple"""
    print(Color.CIAN + "╔" + "═" * (ANCHO - 2) + "╗" + Color.RESET)
    print(Color.CIAN + "║" + Color.RESET + texto.center(ANCHO - 2) + Color.CIAN + "║" + Color.RESET)
    print(Color.CIAN + "╚" + "═" * (ANCHO - 2) + "╝" + Color.RESET)


# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0


titulo("🚴  CALCULADORA DE KILÓMETROS")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # ------------------------------------------------------------------
    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    # ------------------------------------------------------------------
    try:
        meta_km = input(Color.NEGRITA + "¿Cuál es tu meta de kilómetros?: " + Color.RESET)
        meta_km = float(meta_km)

        numero_pedaladas = input(Color.NEGRITA + "¿Cuántas pedaladas has dado?: " + Color.RESET)
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print(Color.ROJO + "Entrada inválida. Por favor, introduce solo números." + Color.RESET)
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # ------------------------------------------------------------------
    # Ahora hacemos los cálculos
    # ------------------------------------------------------------------

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # ------------------------------------------------------------------
    # Operaciones de salida
    # ------------------------------------------------------------------
    print()
    linea()
    print(f"Has dado {Color.NEGRITA}{numero_pedaladas}{Color.RESET} pedaladas")
    print(f"Cada pedalada son {Color.NEGRITA}{metros_por_pedalada}{Color.RESET} metros")
    print(f"Pues has avanzado {Color.NEGRITA}{avance_km:.2f} km{Color.RESET}")
    print(f"Tu meta es de {Color.NEGRITA}{meta_km:.2f} km{Color.RESET}")
    linea()
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print(Color.VERDE + Color.NEGRITA + "🎉 ¡Felicidades! Has alcanzado tu meta 🎉" + Color.RESET)

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print(Color.VERDE + f"Incluso has hecho {kilometros_extra:.2f} km de más. ¡Enhorabuena!" + Color.RESET)
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print(Color.AMARILLO + f"Todavía no has alcanzado tu meta." + Color.RESET)
        print(Color.AMARILLO + f"Te faltan {kilometros_restantes:.2f} km para conseguirlo. ¡Sigue así!" + Color.RESET)

    # Preguntamos si el usuario quiere hacer otro cálculo o salir del programa
    print()
    continuar = input(Color.NEGRITA + "¿Quieres calcular otra vez? (s/n): " + Color.RESET)

    # Si no responde "s", rompemos el bucle y terminamos el programa
    if continuar.lower() != "s":
        print()
        print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
        break
