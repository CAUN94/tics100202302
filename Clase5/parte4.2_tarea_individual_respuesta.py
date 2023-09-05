import random

def juego_jalisco():
    print("Piensa en un número entre 1 y 100. Jalisco intentará adivinarlo.")
    inicio = 1
    fin = 100

    for intentos in range(7):
        suposicion = random.randint(inicio, fin)
        respuesta = input(f"¿Es {suposicion} tu número? (mayor/menor/igual): ")

        if respuesta == "igual":
            print(f"¡Jalisco adivinó tu número en {intentos + 1} intentos!")
            return
        elif respuesta == "mayor":
            inicio = suposicion + 1
        elif respuesta == "menor":
            fin = suposicion - 1
        else:
            print("Respuesta no válida. Por favor, ingresa 'mayor', 'menor' o 'igual'.")

    print("Jalisco no pudo adivinar tu número. ¡Buena jugada!")

juego_jalisco()