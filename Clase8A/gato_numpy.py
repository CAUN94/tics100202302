import numpy as np

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print(tablero)

# Sin Numpy
# def mostrar_tablero_sin_numpy(tablero):
#     for i in range(len(tablero)):
#         for j in range(len(tablero[i])):
#             print(tablero[i][j], end=" ")
#         print()

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero,jugador_actual):
    # Verificar filas
    for i in range(0,3):
        if tablero[i,0] == tablero[i,1] == tablero[i,2] == jugador_actual:
            return True
    # Verificar columnas
    for j in range(0,3):
        if tablero[0,j] == tablero[1,j] == tablero[2,j] == jugador_actual:
            return True

    # Verificar diagonal principal
    if tablero[0,0] == tablero[1,1] == tablero[2,2] == jugador_actual:
        return True

    # Verificar diagonal secundaria
    if tablero[0,2] == tablero[1,1] == tablero[2,0] == jugador_actual:
        return True

    return False
# Inicio del programa, creacion de tablero
# y definicion de jugador actual

# Tabler es una matriz de 3x3 con ceros
tablero = np.full([3,3]," ")
jugador_actual = 'X'
jugadas = 0

while True:
    mostrar_tablero(tablero)
    fila = int(input("Ingrese fila (0,1,2): " + jugador_actual + ":"))
    columna = int(input("Ingrese columna(0,1,2): " + jugador_actual + ":"))

    # Verificar que las coordenadas sean validas
    while fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Coordenadas invalidas")
        fila = int(input("Ingrese fila (0,1,2): " + jugador_actual + ":"))
        columna = int(input("Ingrese columna (0,1,2): " + jugador_actual + ":"))
    if tablero[fila,columna] == " ":
        tablero[fila,columna] = jugador_actual
        jugadas += 1
        if verificar_ganador(tablero,jugador_actual):
            print("Gano " + jugador_actual)
            mostrar_tablero(tablero)
            break
        elif jugadas == 9:
            print("Empate")
            mostrar_tablero(tablero)
            break

        if jugador_actual == 'X':
            jugador_actual = 'O'
        else:
            jugador_actual = 'X'
    else:
        print("Esta casilla ya esta ocupada")
        print("Ingrese nuevamente")

