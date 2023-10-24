import numpy as np

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print(tablero)

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for i in range(0,3):
        if tablero[i, 0] == tablero[i, 1] == tablero[i, 2] == jugador:
            return True

    # Verificar columnas
    for j in range(0,3):
        if tablero[0, j] == tablero[1, j] == tablero[2, j] == jugador:
            return True

    # Verificar diagonal principal
    if tablero[0, 0] == tablero[1, 1] == tablero[2, 2] == jugador:
        return True

    # Verificar diagonal secundaria
    if tablero[0, 2] == tablero[1, 1] == tablero[2, 0] == jugador:
        return True

    return False


# Inicio del programa, creacion de tablero
# y definicion de jugador actual

tablero = np.full((3,3)," ")
jugador_actual = "X"
jugadas = 0

while True:
    mostrar_tablero(tablero)
    
    fila = int(input("Fila (0, 1, 2) para " + jugador_actual + ": "))
    columna = int(input("Columna (0, 1, 2) para " + jugador_actual + ": "))


    while fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Ingresa una fila y columna válida (0, 1, 2).")
        fila = int(input("Fila (0, 1, 2) para " + jugador_actual + ": "))
        columna = int(input("Columna (0, 1, 2) para " + jugador_actual + ": "))

    if tablero[fila, columna] == " ":
        tablero[fila, columna] = jugador_actual
        jugadas += 1

        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print("¡" + jugador_actual + " ha ganado!")
            break
        elif jugadas == 9:
            mostrar_tablero(tablero)
            print("¡Es un empate!")
            break

        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
