# TAREA
# El siguiente juego es el conocido "juego de la vida" el cual debera 
# reescribir para ser utilizado en Pygame!

import numpy as np
import time

# Configuración del tablero
filas = 10
columnas = 10
generaciones = 50
delay = 0.5  # Segundos de retraso entre generaciones

# Función para inicializar el tablero con células vivas y muertas aleatorias
def inicializar_tablero(filas, columnas):
    return np.random.randint(0,2,(filas, columnas))

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        for celula in fila:
            if celula == 1:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print("")

# Función para calcular el próximo estado del tablero
def siguiente_generacion(tablero):
    filas = tablero.shape[0]
    columnas = tablero.shape[1]
    nuevo_tablero = np.zeros((filas, columnas))
    
    for fila in range(filas):
        for columna in range(columnas):
            celula_actual = tablero[fila, columna]
            vecinos_vivos = 0

            # Contar vecinos vivos
            for i in range(-1, 2):
                for j in range(-1, 2):
                    vecino_fila = fila + i
                    vecino_columna = columna + j

                    # Comprobar límites del tablero
                    if 0 <= vecino_fila < filas and 0 <= vecino_columna < columnas:
                        vecinos_vivos += tablero[vecino_fila, vecino_columna]

            # Aplicar reglas del juego de la vida
            if celula_actual == 1:
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nuevo_tablero[fila, columna] = 0
                else:
                    nuevo_tablero[fila, columna] = 1
            elif celula_actual == 0 and vecinos_vivos == 3:
                nuevo_tablero[fila, columna] = 1

    return nuevo_tablero



# Juego de la vida
tablero = inicializar_tablero(filas, columnas)
for generacion in range(0,generaciones):
    print(f"Generación {generacion + 1}:")
    imprimir_tablero(tablero)
    tablero = siguiente_generacion(tablero)
    time.sleep(delay)
