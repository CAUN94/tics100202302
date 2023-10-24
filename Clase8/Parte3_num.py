# Algo que vimos de manera superficial fueron los "ciclos for anidados" con los
# cuales podemos, dentro de otras cosas, trabajar con "matrices" o "listas de listas"
# ejemplo:

lista1 = [[1,1,1],[1,1,1],[1,1,1]]
largo_lista = len(lista1)
for i in range (0,largo_lista):
    print(lista1[i]) 
"""
Lo anterior entregaria la siguiente matriz
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
"""
# Al igual que en el caso anterior, numpy tiene una forma mas resumida:

import numpy

matriz = numpy.ones([3,3])
print(matriz)

##############################################################################

# Como seria el juego "gato" en estos casos?

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" | ")
        print("")
        print("-" * 13)

# Función para verificar si alguien ha ganado 
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        ganador = True
        for casilla in fila:
            if casilla != jugador:
                ganador = False
                break
        if ganador:
            return True

    # Verificar columnas
    for columna in range(0,3):
        ganador = True
        for fila in range(0,3):
            if tablero[fila][columna] != jugador:
                ganador = False
                break
        if ganador:
            return True

    # Verificar diagonales
    ganador = True
    for i in range(3):
        if tablero[i][i] != jugador:
            ganador = False
            break
    if ganador:
        return True
    
    ganador = True
    for i in range(3):
        if tablero[i][2 - i] != jugador:
            ganador = False
            break
    if ganador:
        return True

    return False

# Inicio del programa, creacion de tablero
# y definicion de jugador actual
tablero = []
for i in range(0,3):
    fila = []
    for j in range(0,3):
        fila.append(" ")
    tablero.append(fila)
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

    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador_actual
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


