# Supongamos que queremos replicar el juego "piedra, papel o tijeras" (cachipun!!!!!)
# La condicion para que el juego termina es el ganador de 3 rondas (no consecutivas). 
# Concideremos para este caso que jugaremos contra el PC

import random

# Inicialización de las puntuaciones de los jugadores
puntuacion_jugador = 0
puntuacion_PC = 0

while (puntuacion_jugador < 3) and (puntuacion_PC < 3):
    # Elección del jugador
    print("""Elige una opción:
    1. Piedra
    2. Papel
    3. Tijeras""")
    
    eleccion_jugador = int(input("Ingrese el número de su elección: "))
    
    # Elección aleatoria de la computadora
    eleccion_PC = random.randint(1, 3)

    # Determinar el resultado de la ronda
    if eleccion_jugador == eleccion_PC:
        print("Empate")
    elif (eleccion_jugador == 1 and eleccion_PC == 3):
        puntuacion_jugador += 1
        print("Buena!, Ganaste esta ronda!")
    elif (eleccion_jugador == 2 and eleccion_PC == 1):
        puntuacion_jugador += 1 
        print("Buena!, Ganaste esta ronda!")
    elif (eleccion_jugador == 3 and eleccion_PC == 2):
        print("Buena!, Ganaste esta ronda!")
        puntuacion_jugador += 1
    else:
        print("Perdiste!, el PC Gana esta ronda!")
        puntuacion_PC += 1
    print(f"Puntuacion jugador: {puntuacion_jugador} ; Puntuacion PC {puntuacion_PC}")
# Determinar el ganador del juego
print("#######################################################")
if puntuacion_jugador > puntuacion_PC:
    print("Felicitaciones! ganaste un sobre de mermelada!!!")
else:
    print("Perdedor!!!!.. Sera para la otra ;) ")

